from collections import defaultdictimport enumimport randomfrom date_and_time import TimeSpan, create_time_spanfrom elements import SleepElement, GeneratorElementfrom gsi_handlers.story_progression_handlers import is_story_progression_pass_archive_enabled, GSIStoryProgressionPassData, archive_story_progression_pass_data, GSIStoryProgressionArcDatafrom interactions.utils.death import DeathTypefrom scheduling import Timelinefrom sims4.localization import TunableLocalizedStringFactoryVariantfrom sims4.resources import Typesfrom sims4.service_manager import Servicefrom sims4.tuning.tunable import TunableList, TunableRealSecond, TunableTuple, TunableReference, TunableRange, TunableEnumEntry, TunableVariant, TunablePercent, TunableInterval, Tunable, TunableMappingfrom sims4.utils import classpropertyfrom story_progression import StoryProgressionFlags, StoryProgressionArcSeedReason, story_progression_telemetryfrom story_progression.actions import TunableStoryProgressionActionVariantimport alarmsimport clockimport persistence_error_typesimport servicesimport simsimport sims4.randomimport sims4.logimport zone_typesfrom story_progression.story_progression_demographics import SimTestDemographicFunction, TotalSimDemographicFunction, ResidentialLotDemographicFunctionfrom story_progression.story_progression_enums import StoryTypefrom story_progression.story_progression_result import StoryProgressionResult, StoryProgressionResultTypefrom story_progression.story_progression_rule_set import StoryProgressionRuleSetfrom story_progression.story_progression_log import log_story_progression_demographicsfrom story_progression.story_progression_tuning import StoryProgTunablesfrom tunable_time import TunableTimeOfDay, TunableTimeSpanlogger = sims4.log.Logger('StoryProgression')
class StoryProgressionPassType(enum.Int):
    GLOBAL = 0
    PER_WORLD = 1

class StoryProgressionService(Service):
    INTERVAL = TunableRealSecond(description='\n        The time between Story Progression actions. A lower number will\n        impact performance.\n        ', default=5)
    ACTIONS = TunableList(description='\n        A list of actions that are available to Story Progression.\n        ', tunable=TunableStoryProgressionActionVariant())
    FEATURE_KEY = 14347699396486965923

    @staticmethod
    def _verify_tunable_callback(instance_class, tunable_name, source, value):
        for pass_data in value:
            previous_value = None
            for demographic_data in pass_data.demographic_data:
                if previous_value >= demographic_data.maximum_range:
                    logger.error('Maximum range values in demographic data within pass {} must be in increasing order: {} > {}', pass_data.debug_pass_name, previous_value*100, demographic_data.maximum_range*100)
                    break
                previous_value = demographic_data.maximum_range
            if previous_value < 1:
                logger.error('Maximum range value within pass {} does not reach 100.  This means there is a hole in the data that must be filled.', pass_data.debug_pass_name)

    STORY_PROGRESSION_PASSES = TunableList(description='\n        A list of the different Story Progression Passes that\n        are used to attempt to seed new Story Arcs upon Sims.\n        ', tunable=TunableTuple(description='\n            Data related to a single Story Progression Pass.\n            ', pass_type=TunableEnumEntry(description='\n                The different type of pass this is.\n                GLOBAL: This pass will run a single time and interact\n                with Sims/Households/Lots across the entire game.\n                PER_WORLD: This pass will run multiple times, once\n                per world and only interact with Sims/Households/Lots on\n                that world.\n                ', tunable_type=StoryProgressionPassType, default=StoryProgressionPassType.GLOBAL), potential_arcs=TunableList(description='\n                A weighted list of the potential story arcs\n                to try and seed.\n                ', tunable=TunableTuple(description='\n                    A pair of a potential story arc and the\n                    weight of that story arc being selected.\n                    ', story_arc=TunableReference(description='\n                        The story arc that might be chosen.\n                        ', manager=services.get_instance_manager(Types.STORY_ARC), pack_safe=True), weight=TunableRange(description='\n                        The chance that this story arc will be chosen.\n                        ', tunable_type=int, default=1, minimum=1))), demographic_function=TunableVariant(description='\n                The different demographic function that we will use in order to\n                determine the chance of one of these arcs being seeded.\n                \n                Each of these functions will return a percentage of sims/households/lots\n                that fit the question out of a total.  This percentage is then used with\n                the demographic data to determine exactly what to do.\n                ', sim_test=SimTestDemographicFunction.TunableFactory(), total_sim=TotalSimDemographicFunction.TunableFactory(), residential_lot=ResidentialLotDemographicFunction.TunableFactory(), default='sim_test'), demographic_data=TunableList(description='\n                A grouping of the different instructions of what this pass should do at\n                every demographic value given by the demographic function.\n                ', tunable=TunableTuple(description='\n                    A group of demographic data.  Each set of demographic data should have a maximum range\n                    higher than the previous one.\n                    ', maximum_range=TunablePercent(description='\n                        The maximum value of this range of demographic data within the pass tuning.\n                        Each maximum range should be larger than the one before it in order to create\n                        the ranges where each set of demographic data is used.  The demographic function\n                        ends up returning a percentage which we then use these values to determine which\n                        data set we want to use based on that percentage.\n                        ', default=100), chance_of_occurrence=TunablePercent(description='\n                        The chance that we attempt to seed an arc at all during this pass\n                        at this demographic level.\n                        ', default=100), number_to_seed=TunableInterval(description='\n                        The number of arcs to seed.  A random value between min and max will be chosen\n                        as the number we will seed.\n                        ', tunable_type=int, default_lower=1, default_upper=3, minimum=0))), debug_pass_name=Tunable(description='\n                Name of this pass for use within logs and the GSI for easier debugging.\n                ', tunable_type=str, default='')), verify_tunable_callback=_verify_tunable_callback)
    UPDATE_TIME = TunableTimeOfDay(description='\n        The time of day that the story progression service\n        will seed new arcs and update the existing ones.\n        ')

    def __init__(self):
        self._alarm_handle = None
        self._next_action_index = 0
        self._story_progression_flags = StoryProgressionFlags.DISABLED
        self._demographics = None
        self._timeline = None
        self._timeline_update = None
        self._timeline_multiplier = 1
        self._update_story_progression_element = None
        self._sim_story_progression_trackers = set()
        self._historical_sim_story_progression_trackers = set()
        self._household_story_progression_trackers = set()
        self._historical_household_story_progression_trackers = set()
        self.protected_households_rule_set = None
        self.unprotected_households_rule_set = None
        self._story_progression_enabled_in_options = True
        self._story_progression_enabled_via_killswitch = True

    @classproperty
    def save_error_code(cls):
        return persistence_error_types.ErrorCodes.SERVICE_SAVE_FAILED_STORY_PROGRESSION_SERVICE

    @property
    def story_progression_enabled(self):
        return self._story_progression_enabled_in_options and self._story_progression_enabled_via_killswitch

    def load_options(self, options_proto):
        if options_proto is None:
            return
        self._story_progression_enabled_in_options = options_proto.story_progression_effects_enabled

    def setup(self, save_slot_data=None, **kwargs):
        if save_slot_data is not None:
            sims.global_gender_preference_tuning.GlobalGenderPreferenceTuning.enable_autogeneration_same_sex_preference = save_slot_data.gameplay_data.enable_autogeneration_same_sex_preference
            story_progression_data = save_slot_data.gameplay_data.story_progression_service
            for action in StoryProgressionService.ACTIONS:
                action.load(story_progression_data)

    def save(self, save_slot_data=None, **kwargs):
        if save_slot_data is not None:
            save_slot_data.gameplay_data.enable_autogeneration_same_sex_preference = sims.global_gender_preference_tuning.GlobalGenderPreferenceTuning.enable_autogeneration_same_sex_preference
            story_progression_data = save_slot_data.gameplay_data.story_progression_service
            for action in StoryProgressionService.ACTIONS:
                action.save(story_progression_data)

    def load(self, zone_data=None):
        save_game_proto = services.get_persistence_service().get_save_game_data_proto()
        self.protected_households_rule_set = StoryProgressionRuleSet(save_game_proto.protected_households_story_progression_rule_set)
        self.unprotected_households_rule_set = StoryProgressionRuleSet(save_game_proto.unprotected_households_story_progression_rule_set)

    def on_all_households_and_sim_infos_loaded(self, client):
        self.update()
        sim_timeline = services.time_service().sim_timeline
        now = sim_timeline.now
        when = now.time_of_next_day_time(self.UPDATE_TIME)
        self._update_story_progression_element = sim_timeline.schedule(GeneratorElement(self._update_gen), when=when)
        return super().on_all_households_and_sim_infos_loaded(client)

    def enable_story_progression_flag(self, story_progression_flag):
        self._story_progression_flags |= story_progression_flag

    def disable_story_progression_flag(self, story_progression_flag):
        self._story_progression_flags &= ~story_progression_flag

    def is_story_progression_flag_enabled(self, story_progression_flag):
        return self._story_progression_flags & story_progression_flag

    def on_client_connect(self, client):
        current_zone = services.current_zone()
        current_zone.refresh_feature_params(feature_key=self.FEATURE_KEY)
        current_zone.register_callback(zone_types.ZoneState.RUNNING, self._initialize_alarm)
        current_zone.register_callback(zone_types.ZoneState.SHUTDOWN_STARTED, self._on_zone_shutdown)

    def _on_zone_shutdown(self):
        current_zone = services.current_zone()
        if self._alarm_handle is not None:
            alarms.cancel_alarm(self._alarm_handle)
        current_zone.unregister_callback(zone_types.ZoneState.SHUTDOWN_STARTED, self._on_zone_shutdown)
        if self._update_story_progression_element is not None:
            self._update_story_progression_element.trigger_hard_stop()
            self._update_story_progression_element = None

    def _initialize_alarm(self):
        current_zone = services.current_zone()
        current_zone.unregister_callback(zone_types.ZoneState.RUNNING, self._initialize_alarm)
        time_span = clock.interval_in_sim_minutes(self.INTERVAL)
        self._alarm_handle = alarms.add_alarm(self, time_span, self._process_next_action, repeating=True)

    def _process_next_action(self, _):
        self.process_action_index(self._next_action_index)
        self._next_action_index += 1
        if self._next_action_index >= len(self.ACTIONS):
            self._next_action_index = 0

    def process_action_index(self, index):
        if index >= len(self.ACTIONS):
            logger.error('Trying to process index {} where max index is {}', index, len(self.ACTIONS) - 1)
            return
        action = self.ACTIONS[index]
        if action.should_process(self._story_progression_flags):
            action.process_action(self._story_progression_flags)

    def process_all_actions(self):
        for i in range(len(self.ACTIONS)):
            self.process_action_index(i)

    def set_time_multiplier(self, time_multiplier):
        if time_multiplier < 0:
            logger.error('Unable to set Story Progression time multiplier to {}', time_multiplier)
            return
        self._timeline_multiplier = time_multiplier

    def update(self):
        current_time = services.time_service().sim_now
        if self._timeline is None:
            self._timeline = Timeline(current_time)
        if self._timeline_update is None:
            self._timeline_update = current_time
            return
        delta_time = current_time - self._timeline_update
        self._timeline_update = current_time
        delta_time *= self._timeline_multiplier
        self._timeline.simulate(self._timeline.now + delta_time)

    def set_story_progression_enabled_in_options(self, enabled):
        self._story_progression_enabled_in_options = enabled

    def set_story_progression_enabled_via_killswitch(self, enabled):
        self._story_progression_enabled_via_killswitch = enabled

    def _seed_arcs_from_pass_and_neighborhood_gen(self, pass_tuning, neighborhood_proto, timeline, gsi_data, debug_seed_all_arcs=False):
        if not pass_tuning.potential_arcs:
            gsi_data.result = StoryProgressionResult(StoryProgressionResultType.FAILED_NO_ARCS, 'No potential arcs.  All arcs must not be installed or no arcs have been tuned.')
            return
        (demographic_result, sim_infos, household_ids, zone_ids) = pass_tuning.demographic_function(gsi_data, neighborhood_proto_buff=neighborhood_proto)
        if demographic_result is None:
            if timeline is not None:
                yield timeline.run_child(SleepElement(TimeSpan.ZERO))
            gsi_data.result = StoryProgressionResult(StoryProgressionResultType.FAILED_DEMOGRAPHICS, 'No demographic result generated.')
            return
        gsi_data.demographic_percentage = demographic_result
        for potential_demographic_data in pass_tuning.demographic_data:
            if demographic_result <= potential_demographic_data.maximum_range:
                demographic_data = potential_demographic_data
                break
        logger.error('Attempting to use demographic data for pass {} that does not have any data for value {}', pass_tuning.debug_pass_name, demographic_result)
        gsi_data.result = StoryProgressionResult(StoryProgressionResultType.ERROR, 'Attempting to use demographic data for pass {} that does not have any data for value {}', pass_tuning.debug_pass_name, demographic_result)
        return
        if gsi_data is not None and gsi_data is not None and debug_seed_all_arcs or random.random() > demographic_data.chance_of_occurrence:
            if timeline is not None:
                yield timeline.run_child(SleepElement(TimeSpan.ZERO))
            gsi_data.result = StoryProgressionResult(StoryProgressionResultType.FAILED_DEMOGRAPHICS, 'Failed demographic chance of occurrence.')
            return
        if debug_seed_all_arcs:
            number_to_seed = len(pass_tuning.potential_arcs)
        else:
            number_to_seed = demographic_data.number_to_seed.random_int()
            if number_to_seed == 0:
                gsi_data.result = StoryProgressionResult(StoryProgressionResultType.FAILED_DEMOGRAPHICS, 'Demographics decided to seed 0 arcs.')
                return
        potential_arcs = [(potential_arc.weight, potential_arc.story_arc) for potential_arc in pass_tuning.potential_arcs]
        for i in range(number_to_seed):
            if debug_seed_all_arcs:
                chosen_arc_index = i
                logger.error('One of the arcs failed when attempting to seed all arcs.  Not all arcs will have been seeded.')
                break
            else:
                chosen_arc_index = sims4.random.weighted_random_index(potential_arcs)
            potential_arc = potential_arcs[chosen_arc_index][1]
            (sim_candidate, household_candidate, zone_candidate) = potential_arc.select_candidates(sim_infos, household_ids, zone_ids)
            chosen_candidate = None
            if sim_candidate is not None and potential_arc.arc_type == StoryType.SIM_BASED:
                story_progression_tracker = sim_candidate.story_progression_tracker
                chosen_candidate = sim_candidate
            elif household_candidate is not None and potential_arc.arc_type == StoryType.HOUSEHOLD_BASED:
                household_manager = services.household_manager()
                household = household_manager.get(household_candidate)
                story_progression_tracker = household.story_progression_tracker
                chosen_candidate = household_candidate
            else:
                del potential_arcs[chosen_arc_index]
            if story_progression_tracker is None:
                logger.error('Candidate {} had no StoryProgressionTracker when trying to seed story progression arc: {}', chosen_candidate, potential_arc)
                del potential_arcs[chosen_arc_index]
            else:
                result = story_progression_tracker.add_arc(potential_arc, zone_candidate=zone_candidate)
                if not result:
                    logger.warn('Attempting to seed arc {} failed during setup: {}', potential_arc, result.reason)
                    del potential_arcs[chosen_arc_index]
                else:
                    arc_gsi_data = GSIStoryProgressionArcData()
                    arc_gsi_data.arc = potential_arc
                    if potential_arc.arc_type == StoryType.SIM_BASED:
                        arc_gsi_data.item_id = sim_candidate.id
                        arc_gsi_data.item_name = sim_candidate.full_name
                    else:
                        arc_gsi_data.item_id = household.id
                        arc_gsi_data.item_name = household.name
                    gsi_data.arc_data.append(arc_gsi_data)
                    gsi_data.arcs_seeded += 1
                    if gsi_data is not None and zone_candidate is not None and zone_candidate in zone_ids:
                        zone_ids.remove(zone_candidate)
                    if potential_arc.arc_type == StoryType.SIM_BASED:
                        if sim_candidate.id not in self._sim_story_progression_trackers:
                            self._sim_story_progression_trackers.add(sim_candidate.id)
                        if sim_candidate in sim_infos:
                            sim_infos.remove(sim_candidate)
                    else:
                        if household_candidate not in self._household_story_progression_trackers:
                            self._household_story_progression_trackers.add(household_candidate)
                        if household_candidate in household_ids:
                            household_ids.remove(household_candidate)
                    break
                    logger.info('All arcs in pass {} failed to find candidates.', pass_tuning.debug_pass_name)
                    gsi_data.result = StoryProgressionResult(StoryProgressionResultType.FAILED_NO_ARCS, 'All arcs failed to find candidates.')
            break
        if timeline is not None:
            yield timeline.run_child(SleepElement(TimeSpan.ZERO))

    def seed_new_story_arcs_gen(self, timeline=None, debug_seed_all_arcs=False):
        for pass_tuning in self.STORY_PROGRESSION_PASSES:
            if pass_tuning.pass_type == StoryProgressionPassType.GLOBAL:
                neighborhood_protos = (None,)
            else:
                neighborhood_protos = services.get_persistence_service().get_neighborhoods_proto_buf_gen()
            for neighborhood_proto in neighborhood_protos:
                if is_story_progression_pass_archive_enabled():
                    gsi_data = GSIStoryProgressionPassData()
                    gsi_data.story_progression_pass = pass_tuning.debug_pass_name
                else:
                    gsi_data = None
                yield from self._seed_arcs_from_pass_and_neighborhood_gen(pass_tuning, neighborhood_proto, timeline, gsi_data, debug_seed_all_arcs=debug_seed_all_arcs)
                if gsi_data is not None:
                    archive_story_progression_pass_data(gsi_data)
                if debug_seed_all_arcs:
                    break

    def _update_story_progression_trackers_gen(self, tracker_list, manager, timeline=None):
        for story_progression_obj_id in tuple(tracker_list):
            story_progression_obj = manager.get(story_progression_obj_id)
            if story_progression_obj is None:
                tracker_list.remove(story_progression_obj_id)
            else:
                story_progression_tracker = story_progression_obj.story_progression_tracker
                if story_progression_tracker is None:
                    tracker_list.remove(story_progression_obj_id)
                else:
                    yield from story_progression_tracker.update_arcs_gen(timeline=timeline)
                    if not story_progression_tracker.has_arcs:
                        tracker_list.remove(story_progression_obj_id)
                    if timeline is not None:
                        yield timeline.run_child(SleepElement(TimeSpan.ZERO))

    def update_story_progression_trackers_gen(self, timeline=None):
        yield from self._update_story_progression_trackers_gen(self._sim_story_progression_trackers, services.sim_info_manager(), timeline=timeline)
        yield from self._update_story_progression_trackers_gen(self._household_story_progression_trackers, services.household_manager(), timeline=timeline)

    def _update_gen(self, timeline):
        while True:
            reschedule = True
            try:
                if self.story_progression_enabled:
                    yield from self.seed_new_story_arcs_gen(timeline=timeline)
                    yield from self.update_story_progression_trackers_gen(timeline=timeline)
            except GeneratorExit:
                reschedule = False
                raise
            except Exception as exception:
                logger.exception('Exception while updating story progression service.: ', exc=exception)
            finally:
                if reschedule:
                    log_story_progression_demographics()
                    time_span = timeline.now.time_till_next_day_time(self.UPDATE_TIME)
                    time_span = create_time_span(days=1)
                    yield timeline.run_child(SleepElement(time_span))

    def cache_active_arcs_sim_id(self, sim_id):
        self._sim_story_progression_trackers.add(sim_id)

    def cache_active_arcs_household_id(self, household_id):
        self._household_story_progression_trackers.add(household_id)

    def cache_historical_arcs_sim_id(self, sim_id):
        self._historical_sim_story_progression_trackers.add(sim_id)

    def cache_historical_arcs_household_id(self, household_id):
        self._historical_household_story_progression_trackers.add(household_id)

    def get_discovery_string(self):
        sim_info_manager = services.sim_info_manager()
        household_manager = services.household_manager()
        trackers = [(sim_info_manager, self._historical_sim_story_progression_trackers, sim_id) for sim_id in self._historical_sim_story_progression_trackers]
        trackers.extend((household_manager, self._historical_household_story_progression_trackers, household_id) for household_id in self._historical_household_story_progression_trackers)
        while trackers:
            (manager, historical_tracker_list, tracker_id) = trackers.pop(random.randint(0, len(trackers) - 1))
            tracker_owner = manager.get(tracker_id)
            tracker = tracker_owner.story_progression_tracker if tracker_owner is not None else None
            if tracker is None:
                historical_tracker_list.remove(tracker_id)
            else:
                (chapter, tokens) = tracker.get_random_historical_chapter()
                if chapter is None:
                    historical_tracker_list.remove(tracker_id)
                    break
                self._clear_chapter_history(chapter)
                if chapter.discovery is None:
                    pass
                else:
                    story_progression_telemetry.send_chapter_discovered_telemetry(chapter)
                    return (chapter.discovery.string, tokens)
        return (StoryProgTunables.HISTORY.no_history_discovery_string, [])

    def _clear_chapter_history(self, chapter):
        arc = chapter.arc
        arc.try_remove_historical_chapter(chapter)
        if arc.historical_chapters:
            return
        tracker = arc.tracker
        tracker.try_remove_historical_arc(arc)
        if tracker.historical_arcs:
            return
        if tracker.tracker_type is StoryType.SIM_BASED:
            self._historical_sim_story_progression_trackers.remove(tracker.sim_info.id)
        elif tracker.tracker_type is StoryType.HOUSEHOLD_BASED:
            self._historical_household_story_progression_trackers.remove(tracker.household.id)
