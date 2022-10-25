import randomimport servicesimport sims4from animation.animation_constants import CreatureTypefrom distributor.rollback import ProtocolBufferRollbackfrom event_testing.resolver import GlobalResolverfrom event_testing.tests import TunableTestSetfrom objects.components.state import ObjectStateValuefrom objects.components.types import ANIMAL_OBJECT_COMPONENT, STATE_COMPONENT, ANIMAL_HOME_COMPONENT, TOOLTIP_COMPONENT, NAME_COMPONENTfrom persistence_error_types import ErrorCodesfrom protocolbuffers import GameplaySaveData_pb2from scheduler import WeeklySchedulefrom sims4.common import Packfrom sims4.service_manager import Servicefrom sims4.tuning.tunable import TunableEnumEntry, TunableInterval, TunableList, TunablePackSafeReference, TunableRange, TunableTuplefrom sims4.utils import classpropertyimport build_buylogger = sims4.log.Logger('Animal Service', default_owner='skorman')
class AnimalHomeData:

    def __init__(self, animal_home_id, max_occupancy, animal_types, persist_assignment, owner_household_id, zone_id, open_street_id, current_occupancy=0):
        self.id = animal_home_id
        self.current_occupancy = current_occupancy
        self.current_occupancy_by_type = {}
        self.max_occupancy = max_occupancy
        self.animal_types = animal_types
        self.persist_assignment_in_household_inventory = persist_assignment
        self.owner_household_id = owner_household_id
        self.zone_id = zone_id
        self.open_street_id = open_street_id

    def update_occupancy(self, animal_type, add):
        if add:
            self.current_occupancy += 1
            self.current_occupancy_by_type[animal_type] = self.current_occupancy_by_type.get(animal_type, 0) + 1
        else:
            if self.current_occupancy <= 0:
                logger.error('Attempting to remove an animal from empty home with ID {}.', self.id)
            self.current_occupancy -= 1
            self.current_occupancy_by_type[animal_type] = self.current_occupancy_by_type.get(animal_type) - 1

    def update(self, home_id):
        home = services.object_manager().get(home_id)
        if home is None:
            return
        home_component = home.get_component(ANIMAL_HOME_COMPONENT)
        if home_component is None:
            logger.error('Attempting to update Home {} with no AnimalHomeComponent.', home)
            return
        zone = services.current_zone()
        animal_service = services.animal_service()
        if zone is not None:
            self.zone_id = zone.id
            self.open_street_id = zone.open_street_id
            if zone.is_zone_loading and animal_service is not None:
                animal_service._delayed_home_updates.add(home_id)
            else:
                self.owner_household_id = home.get_household_owner_id()
        if self.max_occupancy is not None:
            return
        self.max_occupancy = home_component.get_max_capacity()
        self.animal_types = home_component.get_eligible_animal_types()
        self.persist_assignment_in_household_inventory = home_component.persist_assignment_in_household_inventory

    def delayed_update(self):
        home = services.object_manager().get(self.id)
        if home is None:
            return
        self.owner_household_id = home.get_household_owner_id()
        zone = services.get_zone(self.zone_id)
        self.open_street_id = zone.open_street_id

class AnimalService(Service):

    @staticmethod
    def _verify_tunable_callback(instance_class, tunable_name, source, value):
        animal_types = {}
        for auto_assignment_schedule in AnimalService.AUTO_ASSIGN_NEW_INHABITANTS:
            if auto_assignment_schedule.animal_type in animal_types.keys():
                logger.error('Animal type {} tuned more than once in AUTO_ASSIGN_NEW_INHABITANTS', auto_assignment_schedule.animal_type)
            animal_types[auto_assignment_schedule.animal_type] = True

    GARDENING_HELP_STATE = ObjectStateValue.TunableReference(description='\n        The gardening help state that animals have when\n        gardening help is enabled.\n        ')
    GARDENING_HELP_WEED_STATES = TunableList(description='\n        For animals with gardening help enabled,\n        these are the relevant weed states on plants to watch for.                 \n        ', tunable=ObjectStateValue.TunableReference())
    GARDENING_HELP_ANIMAL_STATES = TunableList(description="\n        For animals with gardening help enabled, these are the states that\n        an animal will transition from/to whenever the plant's state changes.\n        The order of these lists is the preference in the animal to pick.\n        ", tunable=TunableTuple(animal_type=TunableEnumEntry(tunable_type=CreatureType, default=CreatureType.Rabbit, invalid_enums=(CreatureType.Invalid,)), states=TunableList(tunable=TunableTuple(from_state=ObjectStateValue.TunableReference(), to_state=ObjectStateValue.TunableReference()))))
    AUTO_ASSIGN_NEW_INHABITANTS = TunableList(description='\n        On a schedule, automatically assigns new animals to existing homes\n        that have vacancy. The assignment will try to assign existing homeless\n        animals before creating new animals. \n        ', tunable=TunableTuple(animal_type=TunableEnumEntry(description='\n                The animal home type to scan for on the existing lot.\n                ', tunable_type=CreatureType, default=CreatureType.Rabbit), weekly_schedule=WeeklySchedule.TunableFactory(description='\n                Determines when to trigger the auto-assignment.\n                '), num_assignments_per_home=TunableInterval(description='\n                The number of auto-assignments per home. The value is a random number\n                between the lower and upper bounds, inclusively.\n                ', tunable_type=int, default_lower=1, default_upper=1, minimum=0), max_homes_to_assign=TunableInterval(description='\n                When auto-assignment triggers, this is the maximum number of homes to\n                randomly pick. Homes at max capacity are excluded. The value is a random\n                number between the lower and upper bounds, inclusively.\n                \n                For example:\n                The value is randomly 3.\n                15 homes are on the lot (10 empty or partially full, 5 full)\n                From the 10 homes, 3 are randomly picked for auto-assignment.\n                ', tunable_type=int, default_lower=1, default_upper=1, minimum=0), tests=TunableTestSet(description='\n                Conditional tests to determine if auto-assignment occurs.\n                ')), verify_tunable_callback=_verify_tunable_callback)
    MAX_EMPTY_HOMES_TO_POPULATE = TunableTuple(description='\n        Some Animal Home Component objects are configured to populate empty homes\n        for the following conditions. These settings configure the maximum number\n        of empty homes that can be populated at one time.\n        ', on_new_homes=TunableRange(description='\n            The limit on number of new homes to populate if placed during Build/Buy.\n            ', tunable_type=int, default=5, minimum=0, maximum=5), on_zone_load=TunableRange(description='\n            The limit on number of empty homes to populate after zone load.\n            ', tunable_type=int, default=5, minimum=0, maximum=5))
    AGING_STATISTIC = TunablePackSafeReference(description='\n        The statistic we are operating on.\n        ', manager=services.get_instance_manager(sims4.resources.Types.STATISTIC), class_restrictions=('Commodity',))

    def __init__(self):
        self._animal_assignment_map = {}
        self._objs_destroyed_in_bb = {}
        self._weed_eligible_plants = []
        self._registered_homes = {}
        self._registered_animals = {}
        self._home_ids_registered_in_bb = []
        self._active_weekly_schedules = []
        self._creature_aging_enabled = True
        self._delayed_home_updates = set()

    def start(self):
        self._start_auto_assignment_schedules()

    def stop(self):
        self._stop_auto_assignment_schedules()

    @classproperty
    def required_packs(cls):
        return (Pack.EP11,)

    @property
    def animal_assignment_map(self):
        return self._animal_assignment_map

    @classproperty
    def save_error_code(cls):
        return ErrorCodes.SERVICE_SAVE_FAILED_ANIMAL_SERVICE

    def save(self, save_slot_data=None, **kwargs):
        service_data = GameplaySaveData_pb2.PersistableAnimalService()
        object_manager = services.object_manager()
        for (animal_id, home_data) in self._animal_assignment_map.items():
            if services.current_zone().is_in_build_buy and self._is_obj_destroyed_in_bb(animal_id):
                pass
            else:
                with ProtocolBufferRollback(service_data.animal_data) as animal_data:
                    animal_data.obj_id = animal_id
                    animal_data.animal_type = self._registered_animals[animal_id]
                    if home_data is not None:
                        home_id = home_data.id
                        if services.current_zone().is_in_build_buy:
                            if self._is_obj_destroyed_in_bb(home_id):
                                continue
                            if self._is_obj_modified_in_bb(animal_id) or self._is_obj_modified_in_bb(home_id):
                                animal = object_manager.get(animal_id)
                                home = object_manager.get(home_id)
                                if animal is None or home is None:
                                    continue
                        animal_data.home_id = home_id
                        if home_data.owner_household_id is not None:
                            animal_data.owner_household_id = home_data.owner_household_id
                        if home_data.zone_id is not None:
                            animal_data.zone_id = home_data.zone_id
                        if home_data.open_street_id is not None:
                            animal_data.open_street_id = home_data.open_street_id
        save_slot_data.gameplay_data.animal_service = service_data

    def load(self, **_):
        save_slot_data_msg = services.get_persistence_service().get_save_slot_proto_buff()
        if not save_slot_data_msg.gameplay_data.HasField('animal_service'):
            return
        service_data = save_slot_data_msg.gameplay_data.animal_service
        for animal_data in service_data.animal_data:
            self._registered_animals[animal_data.obj_id] = animal_data.animal_type
            if animal_data.HasField('home_id'):
                home_data = self._registered_homes.get(animal_data.home_id)
                if home_data is None:
                    owner_household_id = None
                    zone_id = None
                    open_street_id = None
                    if animal_data.owner_household_id != 0:
                        owner_household_id = animal_data.owner_household_id
                    if animal_data.zone_id != 0:
                        zone_id = animal_data.zone_id
                    if animal_data.open_street_id != 0:
                        open_street_id = animal_data.open_street_id
                    home_data = AnimalHomeData(animal_data.home_id, None, None, True, owner_household_id, zone_id, open_street_id)
                    self._registered_homes[animal_data.home_id] = home_data
            else:
                home_data = None
            self._move_animal_home(animal_data.obj_id, home_data)

    def load_options(self, options_proto):
        self._creature_aging_enabled = options_proto.creature_aging_enabled

    def save_options(self, options_proto):
        options_proto.creature_aging_enabled = self._creature_aging_enabled

    def update_aging(self):
        for animal_id in self._registered_animals.keys():
            animal = services.object_manager().get(animal_id)
            if animal is None:
                animal = services.inventory_manager().get(animal_id)
            if animal is None:
                pass
            else:
                self.update_animal_aging(animal)

    def update_animal_aging(self, animal):
        aging_statistic = animal.get_stat_instance(self.AGING_STATISTIC)
        if aging_statistic is None:
            return
        aging_statistic.decay_enabled = self._creature_aging_enabled

    def set_aging_enabled(self, enabled):
        self._creature_aging_enabled = enabled
        self.update_aging()

    def on_zone_load(self):
        num_empty_homes_populated = 0
        obj_manager = services.object_manager()
        for (home_id, home_data) in self._registered_homes.items():
            if num_empty_homes_populated >= self.MAX_EMPTY_HOMES_TO_POPULATE.on_zone_load:
                break
            if home_data.current_occupancy > 0:
                pass
            else:
                home = obj_manager.get(home_id)
                if home is None:
                    pass
                elif not home.has_component(ANIMAL_HOME_COMPONENT):
                    logger.error('Registered home {} does not have an Animal Home Component.', home)
                elif home.animalhome_component.try_populate_on_zone_load():
                    num_empty_homes_populated += 1
        for (animal_id, _) in self._animal_assignment_map.items():
            animal_obj = obj_manager.get(animal_id)
            if animal_obj is not None:
                animal_obj.update_object_tooltip()
        for home_id in self._delayed_home_updates:
            home_data = self._registered_homes.get(home_id)
            if home_data is None:
                logger.error('Expecting home {} to be already registered.', home_id)
            else:
                home_data.delayed_update()
        self._delayed_home_updates.clear()

    def on_cleanup_zone_objects(self, client):
        zone = services.current_zone()
        if zone is None:
            return
        household_manager = services.household_manager()
        inventory_manager = services.inventory_manager()
        obj_manager = services.object_manager()
        venue_manager = services.get_instance_manager(sims4.resources.Types.VENUE)
        zone_id = zone.id
        street_id = zone.open_street_id
        current_venue_tuning = venue_manager.get(build_buy.get_current_venue(zone_id))
        lot_owner_household = zone.get_active_lot_owner_household()
        lot_owner_household_id = lot_owner_household.id if lot_owner_household is not None else None
        is_residential = current_venue_tuning.is_residential or current_venue_tuning.is_university_housing
        is_home_in_current_zone_or_street = lambda animal_id, home_data: home_data is None or (home_data.zone_id == zone_id or home_data.open_street_id == street_id)
        assignments_to_check = {animal_id: home_data for (animal_id, home_data) in self._animal_assignment_map.items() if is_home_in_current_zone_or_street(animal_id, home_data)}
        assignments_to_delete = {}
        homeless_animals_to_delete = set()
        for (animal_id, home_data) in assignments_to_check.items():
            animal = obj_manager.get(animal_id) or inventory_manager.get(animal_id)
            if home_data is None:
                if animal is None:
                    assignments_to_delete[animal_id] = True
                elif lot_owner_household is not None and is_residential:
                    pass
                else:
                    household_id = animal.get_household_owner_id()
                    if not household_id is None:
                        if household_manager.get(household_id) is None:
                            homeless_animals_to_delete.add(animal)
                            home_id = home_data.id
                            home = obj_manager.get(home_id)
                            if animal is not None and home is not None:
                                pass
                            else:
                                owner_household_id = home_data.owner_household_id or lot_owner_household_id
                                obj_id_to_check = home_id if home is None else animal_id
                                has_owning_household = owner_household_id is not None and owner_household_id in household_manager
                                if has_owning_household and (home_data.persist_assignment_in_household_inventory and build_buy.is_household_inventory_available(owner_household_id)) and build_buy.object_exists_in_household_inventory(obj_id_to_check, owner_household_id):
                                    pass
                                else:
                                    assignments_to_delete[animal_id] = animal is None
                    homeless_animals_to_delete.add(animal)
                    home_id = home_data.id
                    home = obj_manager.get(home_id)
                    if animal is not None and home is not None:
                        pass
                    else:
                        owner_household_id = home_data.owner_household_id or lot_owner_household_id
                        obj_id_to_check = home_id if home is None else animal_id
                        has_owning_household = owner_household_id is not None and owner_household_id in household_manager
                        if has_owning_household and (home_data.persist_assignment_in_household_inventory and build_buy.is_household_inventory_available(owner_household_id)) and build_buy.object_exists_in_household_inventory(obj_id_to_check, owner_household_id):
                            pass
                        else:
                            assignments_to_delete[animal_id] = animal is None
            else:
                home_id = home_data.id
                home = obj_manager.get(home_id)
                if animal is not None and home is not None:
                    pass
                else:
                    owner_household_id = home_data.owner_household_id or lot_owner_household_id
                    obj_id_to_check = home_id if home is None else animal_id
                    has_owning_household = owner_household_id is not None and owner_household_id in household_manager
                    if has_owning_household and (home_data.persist_assignment_in_household_inventory and build_buy.is_household_inventory_available(owner_household_id)) and build_buy.object_exists_in_household_inventory(obj_id_to_check, owner_household_id):
                        pass
                    else:
                        assignments_to_delete[animal_id] = animal is None
        for (animal_id, should_delete_registration) in assignments_to_delete.items():
            self.remove_animal_assignment(animal_id, should_delete_registration)
        for animal in homeless_animals_to_delete:
            animal.destroy(cause='Destroying homeless unowned animals on load.')
        homes_to_delete = []
        for (home_id, home_data) in self._registered_homes.items():
            if home_data.zone_id != zone_id and home_data.open_street_id != street_id:
                pass
            elif obj_manager.get(home_id) is not None:
                pass
            elif not home_data.current_occupancy:
                homes_to_delete.append(home_id)
        for home_id in homes_to_delete:
            del self._registered_homes[home_id]

    def on_build_buy_exit(self):
        self.fixup_objs_destroyed_in_bb()
        num_empty_homes_populated = 0
        for home_id in self._home_ids_registered_in_bb:
            home = services.object_manager().get(home_id)
            if home is None:
                pass
            else:
                if num_empty_homes_populated >= self.MAX_EMPTY_HOMES_TO_POPULATE.on_new_homes:
                    break
                if not home.has_component(ANIMAL_HOME_COMPONENT):
                    logger.error('Registered home {} does not have an Animal Home Component.', home)
                elif home.animalhome_component.try_populate_on_build_buy_exit():
                    num_empty_homes_populated += 1
        self._home_ids_registered_in_bb.clear()

    def register_home(self, home):
        home_component = home.get_component(ANIMAL_HOME_COMPONENT)
        if home_component is None:
            logger.error('Home {} should have AnimalHomeComponent.', home)
            return False
        home_id = home.id
        zone = services.current_zone()
        new_home = AnimalHomeData(home_id, home_component.get_max_capacity(), home_component.get_eligible_animal_types(), home_component.persist_assignment_in_household_inventory, home.get_household_owner_id(), services.current_zone_id(), zone.open_street_id if zone is not None else None)
        self._registered_homes[home_id] = new_home
        if services.current_zone().is_in_build_buy:
            self._home_ids_registered_in_bb.append(home_id)
        self._update_home_tooltip(home_id)
        name_component = home.get_component(NAME_COMPONENT)
        if name_component is not None:
            name_component.add_name_changed_callback(self._on_home_name_changed)
        return True

    def is_registered_home(self, home_id):
        return home_id in self._registered_homes

    def _update_home_tooltip(self, home_id):
        home_obj = services.object_manager().get(home_id)
        home_data = self._registered_homes[home_id]
        if home_obj is not None and home_obj.has_component(TOOLTIP_COMPONENT):
            home_obj.animalhome_component.update_tooltip(home_data.current_occupancy_by_type)

    def _move_animal_home(self, animal_id, home_data=None):
        prev_home = self._animal_assignment_map.get(animal_id)
        animal_type = self._registered_animals.get(animal_id)
        if animal_type is None:
            logger.error('Object ID {} is not a registered animal.', animal_id)
            return
        if prev_home is not None:
            prev_home.update_occupancy(animal_type, add=False)
            self._update_home_tooltip(prev_home.id)
        self._animal_assignment_map[animal_id] = home_data
        if home_data is not None:
            home_data.update_occupancy(animal_type, add=True)
            self._update_home_tooltip(home_data.id)
        animal = services.object_manager().get(animal_id)
        if animal is not None:
            animal.on_hovertip_requested()

    def _is_valid_for_assignment(self, home, animal):
        if home is None:
            return True
        home_data = self._registered_homes.get(home.id)
        if home_data is None:
            logger.error('Obj {} is not a registered home in the AnimalService.', home)
            return False
        if animal is None:
            logger.error('Animal id {} is not currently instantiated.', animal)
            return False
        if animal.animalobject_component.creature_type not in home_data.animal_types:
            logger.error('Trying to assign animal {} of invalid type {} to home {}', animal, animal.animalobject_component.creature_type, home)
            return False
        elif home_data.current_occupancy >= home_data.max_occupancy:
            return False
        return True

    def _is_obj_destroyed_in_bb(self, obj_id):
        destroy_count = self._objs_destroyed_in_bb.get(obj_id, 0)
        if destroy_count > 0:
            return True
        else:
            return False

    def _is_obj_modified_in_bb(self, obj_id):
        if obj_id not in self._objs_destroyed_in_bb:
            return False
        return self._objs_destroyed_in_bb[obj_id] <= 0

    def assign_animal(self, animal_id, home=None):
        animal = services.object_manager().get(animal_id) or services.inventory_manager().get(animal_id)
        if not (animal_id not in self._animal_assignment_map and (animal is None or animal.has_component(ANIMAL_OBJECT_COMPONENT))):
            logger.error('Obj id {} does not map to a valid animal.', animal_id)
            return False
        if self._is_valid_for_assignment(home, animal) or animal_id in self._registered_animals:
            return
        if animal_id not in self._registered_animals:
            self._registered_animals[animal_id] = animal.animalobject_component.creature_type
        home_data = self._registered_homes.get(home.id) if home is not None else None
        self._move_animal_home(animal_id, home_data)
        return True

    def remove_animal_assignment(self, animal_id, should_delete_registration=False):
        animal_type = self._registered_animals.get(animal_id)
        home_data = self._animal_assignment_map.pop(animal_id, None)
        if animal_type is None or home_data is None:
            return
        if should_delete_registration:
            del self._registered_animals[animal_id]
        home_data.update_occupancy(animal_type, add=False)
        home_id = home_data.id
        self._update_home_tooltip(home_id)
        if not home_data.current_occupancy:
            home_obj = services.object_manager().get(home_id)
            if home_obj is not None and home_obj.has_component(ANIMAL_HOME_COMPONENT):
                home_obj.animalhome_component.try_populate_on_last_inhabitant_removed()

    def transfer_animal_assignment(self, old_animal_id, new_animal_id):
        home_data = self._animal_assignment_map.get(old_animal_id)
        self._move_animal_home(old_animal_id, None)
        self._move_animal_home(new_animal_id, home_data)

    def get_assigned_animal_ids(self, home_id=None):

        def is_assigned(home_data):
            return home_id is None or home_data is not None and home_id == home_data.id

        animal_map = self._animal_assignment_map.items()
        return [animal_id for (animal_id, home_data) in animal_map if is_assigned(home_data)]

    def get_homeless_animal_ids(self):
        animal_map = self._animal_assignment_map.items()
        return [animal_id for (animal_id, home_data) in animal_map if home_data is None]

    def get_homeless_animal_objs(self, animal_type=None, max_amount=None):
        animal_ids = self.get_homeless_animal_ids()
        obj_manager = services.object_manager()
        return_list = []
        for animal_id in animal_ids:
            animal_object = obj_manager.get(animal_id)
            if animal_object is None:
                pass
            else:
                if animal_type is None or animal_type == animal_object.animalobject_component.animal_type_tuning.creature_type:
                    return_list.append(animal_object)
                if max_amount is not None and max_amount == len(return_list):
                    break
        return return_list

    def get_animal_home_id(self, animal_id):
        home_data = self._animal_assignment_map.get(animal_id)
        if home_data is None:
            return
        return home_data.id

    def get_animal_home_max_capacity(self, object_id):
        home_data = self._animal_assignment_map.get(object_id) or self._registered_homes.get(object_id)
        if home_data is None:
            return
        return home_data.max_occupancy

    def get_current_occupancy(self, home_id):
        home_data = self._registered_homes.get(home_id)
        if home_data is None:
            logger.error('Home ID {} is not registered with the AnimalService.', home_id)
            return
        return home_data.current_occupancy

    def find_home_obj_with_vacancy(self, animal_obj):
        for home_obj in services.object_manager().get_all_objects_with_component_gen(ANIMAL_HOME_COMPONENT):
            if self._is_valid_for_assignment(home_obj, animal_obj):
                return home_obj

    def get_animal_home_obj(self, animal):
        home_id = self.get_animal_home_id(animal.id)
        if home_id is None:
            return
        animal_home = services.object_manager().get(home_id) or services.inventory_manager().get(home_id)
        return animal_home

    def get_animal_home_assignee_objs(self, home):
        if home is None:
            return
        if not home.has_component(ANIMAL_HOME_COMPONENT):
            logger.error('Provided home object {} does not have an Animal Home Component.', home)
            return
        obj_manager = services.object_manager()
        inventory_manager = services.inventory_manager()

        def get_obj(assigned_animal_id):
            return obj_manager.get(assigned_animal_id) or inventory_manager.get(assigned_animal_id)

        animal_objs = set(get_obj(animal_id) for animal_id in self.get_assigned_animal_ids(home.id))
        animal_objs.discard(None)
        return animal_objs

    def add_weed_eligible_plant(self, plant_obj):
        if not plant_obj.has_component(STATE_COMPONENT):
            return
        plant_obj.add_state_changed_callback(self._on_plant_object_state_changed)
        self._weed_eligible_plants.append(plant_obj)

    def remove_weed_eligible_plant(self, plant_obj):
        if not plant_obj.has_component(STATE_COMPONENT):
            return
        if plant_obj in self._weed_eligible_plants:
            plant_obj.remove_state_changed_callback(self._on_plant_object_state_changed)
            self._weed_eligible_plants.remove(plant_obj)

    def _on_plant_object_state_changed(self, owner, state, old_value, new_value):
        if old_value == new_value:
            return
        if new_value not in self.GARDENING_HELP_WEED_STATES:
            return
        all_animals_gen = services.object_manager().get_all_objects_with_component_gen(ANIMAL_OBJECT_COMPONENT)
        gardening_help_animals = [animal for animal in all_animals_gen if animal.state_value_active(self.GARDENING_HELP_STATE)]
        if len(gardening_help_animals) == 0:
            return
        for entry in self.GARDENING_HELP_ANIMAL_STATES:
            animals_of_matching_type = [animal for animal in gardening_help_animals if animal.animalobject_component.animal_type_tuning.creature_type == entry.animal_type]
            for state_pair in entry.states:
                animals_of_matching_state = [animal for animal in animals_of_matching_type if animal.state_value_active(state_pair.from_state)]
                if len(animals_of_matching_state) == 0:
                    pass
                else:
                    animal = random.choice(animals_of_matching_state)
                    animal.set_state(state_pair.to_state.state, state_pair.to_state)
                    return

    def _toggle_destroyed_obj(self, obj_id, should_destroy):
        if services.current_zone().is_in_build_buy:
            is_obj_already_destroyed = self._objs_destroyed_in_bb.get(obj_id, 0)
            destroy_op = 1 if should_destroy else -1
            self._objs_destroyed_in_bb[obj_id] = is_obj_already_destroyed + destroy_op

    def on_home_destroyed(self, home_id):
        self._toggle_destroyed_obj(home_id, should_destroy=True)
        if not services.current_zone().is_in_build_buy:
            for animal_id in self.get_assigned_animal_ids(home_id):
                self.assign_animal(animal_id, None)
            del self._registered_homes[home_id]

    def on_home_added(self, home_id):
        self._toggle_destroyed_obj(home_id, should_destroy=False)
        home_data = self._registered_homes.get(home_id)
        if home_data is None:
            home = services.object_manager().get(home_id)
            if home is None:
                logger.error('An unregistered home with ID {} should be instantiated.', home_id)
            self.register_home(home)
            zone = services.current_zone()
            if zone is not None and zone.is_zone_loading:
                self._delayed_home_updates.add(home_id)
            return
        home_data.update(home_id)
        self._update_home_tooltip(home_id)

    def _on_home_name_changed(self, home_object):
        animal_objs = self.get_animal_home_assignee_objs(home_object)
        if animal_objs is None:
            return
        for animal in animal_objs:
            animal.update_object_tooltip()

    def on_animal_destroyed(self, animal_id):
        self._toggle_destroyed_obj(animal_id, should_destroy=True)
        if not services.current_zone().is_in_build_buy:
            self.remove_animal_assignment(animal_id)

    def on_animal_added(self, animal_id):
        self._toggle_destroyed_obj(animal_id, should_destroy=False)
        if services.object_manager().get(animal_id) is None:
            return
        if animal_id not in self._animal_assignment_map:
            self.assign_animal(animal_id, home=None)

    def fixup_objs_destroyed_in_bb(self):
        if not self._objs_destroyed_in_bb:
            return
        ids_to_clear = []
        obj_manager = services.object_manager()
        for (animal_id, home_data) in self._animal_assignment_map.items():
            if home_data is None:
                pass
            else:
                home_id = home_data.id
                if self._is_obj_destroyed_in_bb(home_id):
                    ids_to_clear.append(animal_id)
                else:
                    if not self._is_obj_modified_in_bb(animal_id):
                        if self._is_obj_modified_in_bb(home_id):
                            animal = obj_manager.get(animal_id)
                            home = obj_manager.get(home_id)
                            if not animal is None:
                                if home is None:
                                    ids_to_clear.append(animal_id)
                            ids_to_clear.append(animal_id)
                    animal = obj_manager.get(animal_id)
                    home = obj_manager.get(home_id)
                    if not animal is None:
                        if home is None:
                            ids_to_clear.append(animal_id)
                    ids_to_clear.append(animal_id)
        for animal_id in ids_to_clear:
            self.assign_animal(animal_id, None)
        registrations_to_clear = []
        for (obj_id, destroyed_count) in self._objs_destroyed_in_bb.items():
            if destroyed_count or obj_id in self._home_ids_registered_in_bb and obj_manager.get(obj_id) is None:
                del self._registered_homes[obj_id]
                self._home_ids_registered_in_bb.remove(obj_id)
            elif destroyed_count > 0:
                if obj_id in self._animal_assignment_map:
                    self.remove_animal_assignment(obj_id)
                elif obj_id in self._registered_homes:
                    del self._registered_homes[obj_id]
        self._objs_destroyed_in_bb.clear()

    def _start_auto_assignment_schedules(self):
        for auto_assignment_schedule in self.AUTO_ASSIGN_NEW_INHABITANTS:
            active_weekly_schedule = auto_assignment_schedule.weekly_schedule(start_callback=self._auto_assign_new_inhabitants_from_schedule, extra_data={'animal_type': auto_assignment_schedule.animal_type, 'num_assignments_per_home': auto_assignment_schedule.num_assignments_per_home, 'max_homes_to_assign': auto_assignment_schedule.max_homes_to_assign, 'tests': auto_assignment_schedule.tests})
            self._active_weekly_schedules.append(active_weekly_schedule)

    def _stop_auto_assignment_schedules(self):
        for active_weekly_schedule in self._active_weekly_schedules:
            active_weekly_schedule.destroy()
        self._active_weekly_schedules.clear()

    def _auto_assign_new_inhabitants_from_schedule(self, scheduler, alarm_data, extra_data):
        animal_type = extra_data.get('animal_type')
        num_assignments_per_home = extra_data.get('num_assignments_per_home')
        max_homes_to_assign = extra_data.get('max_homes_to_assign')
        tests = extra_data.get('tests')
        self._auto_assign_new_inhabitants(animal_type, num_assignments_per_home, max_homes_to_assign, tests)

    def _auto_assign_new_inhabitants(self, animal_type, num_assignments_per_home, max_homes_to_assign, tests):

        def _pick_homes(inner_animal_type, num_homes_to_assign):
            if num_homes_to_assign == 0:
                return []
            else:
                eligible_homes = []
                for animal_home_obj in services.object_manager().get_all_objects_with_component_gen(ANIMAL_HOME_COMPONENT):
                    current_occupancy = self.get_current_occupancy(animal_home_obj.id)
                    if inner_animal_type in animal_home_obj.animalhome_component.get_eligible_animal_types() and current_occupancy < animal_home_obj.animalhome_component.get_max_capacity():
                        eligible_homes.append(animal_home_obj)
                if len(eligible_homes) > num_homes_to_assign:
                    return random.sample(eligible_homes, num_homes_to_assign)
                else:
                    return eligible_homes
            return eligible_homes

        def _assign_inhabitants(inner_home, inner_animal_type, num_assignments):
            if num_assignments == 0:
                return
            current_occupancy = self.get_current_occupancy(inner_home.id)
            num_assignments = min(num_assignments, inner_home.animalhome_component.get_max_capacity() - current_occupancy)
            homeless_animals = self.get_homeless_animal_objs(inner_animal_type, num_assignments)
            for homeless_animal in homeless_animals:
                self.assign_animal(homeless_animal.id, inner_home)
            remaining_assignments = num_assignments - len(homeless_animals)
            for i in range(remaining_assignments):
                inner_home.animalhome_component.create_inhabitant()

        if not tests.run_tests(GlobalResolver()):
            return
        homes = _pick_homes(animal_type, max_homes_to_assign.random_int())
        for home in homes:
            _assign_inhabitants(home, animal_type, num_assignments_per_home.random_int())
