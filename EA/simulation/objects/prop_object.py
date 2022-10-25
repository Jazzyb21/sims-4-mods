from objects.base_object import BaseObject
class BasicPropObject(ClientObjectMixin, ReservationMixin, BaseObject):
    VALID_COMPONENTS = ()
    VISIBLE_TO_AUTOMATION = False

    @classproperty
    def is_prop(cls):
        return True

    def __repr__(self):
        return standard_repr(self, self.definition.cls.__name__, self.definition.name or self.definition.id, standard_brief_id_repr(self.id))

    def __str__(self):
        return '[Prop]{}/{}:{}'.format(self.definition.cls.__name__, self.definition.name or self.definition.id, standard_brief_id_repr(self.id))

    @property
    def object_manager_for_create(self):
        return services.prop_manager()

    def can_add_component(self, component_definition):
        return any(component_definition.instance_attr == valid_component_name.instance_attr for valid_component_name in self.VALID_COMPONENTS)

    @property
    def _anim_overrides_internal(self):
        return self.definition.cls._anim_overrides_cls

    @property
    def is_valid_posture_graph_object(self):
        return False

    def supports_posture_type(self, posture_type, *args, is_specific=True, **kwargs):
        return False

    def potential_interactions(self, *_, **__):
        pass

    @property
    def persistence_group(self):
        pass

    @property
    def routing_context(self):
        pass

    def is_surface(self, *args, **kwargs):
        return False

    def get_household_owner_id(self):
        pass

    @property
    def transient(self):
        return False

    @forward_to_components
    def on_state_changed(self, state, old_value, new_value, from_init):
        pass

    def update_component_commodity_flags(self, affordance_provider=None):
        logger.info('Prop object: {} is providing interactions AffordanceProvider:{}', self, affordance_provider)

    @property
    def is_outside(self):
        pass

    @property
    def is_inside_building(self):
        pass

    def is_on_natural_ground(self):
        pass

class PropObject(BasicPropObject, HasStatisticComponent):
    VALID_COMPONENTS = (STATE_COMPONENT, CENSOR_GRID_COMPONENT, STATISTIC_COMPONENT, VIDEO_COMPONENT)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for component_factory in self.definition.cls._components.values():
            if component_factory is not None:
                self.add_component(component_factory(self))

class PropObjectWithFootprint(BasicPropObject, HasFootprintComponent):
    VALID_COMPONENTS = (FOOTPRINT_COMPONENT,)

    def clear_check_line_of_sight_cache(self):
        pass

class PrototypeObject(GameObject):

    @property
    def is_valid_posture_graph_object(self):
        return False
