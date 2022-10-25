import randomimport servicesfrom date_and_time import DateAndTimefrom distributor.rollback import ProtocolBufferRollbackfrom gsi_handlers.story_progression_handlers import is_story_progression_update_archive_enabled, archive_story_progression_update_data, GSIStoryProgressionUpdateDatafrom households.household_tracker import HouseholdTrackerfrom objects import ALL_HIDDEN_REASONSfrom sims.sim_info_tracker import SimInfoTrackerfrom sims4.log import Loggerfrom sims4.resources import Typesfrom sims4.utils import constpropertyfrom story_progression import story_progression_telemetryfrom story_progression.story_progression_enums import StoryTypefrom story_progression.story_progression_exclusivity import StoryProgressionExclusivityfrom story_progression.story_progression_result import StoryProgressionResultTypefrom story_progression.story_progression_tuning import StoryProgTunableslogger = Logger('StoryProgression', default_owner='jjacobson')
class BaseStoryProgressionTracker:

    def __init__(self):
        super().__init__()
        self._current_arcs = None
        self._historical_arcs = None

    @property
    def owner_name(self):
        raise NotImplementedError

    @property
    def current_arcs(self):
        if self._current_arcs is None:
            return tuple()
        return tuple(self._current_arcs)

    @property
    def historical_arcs(self):
        if self._historical_arcs is None:
            return tuple()
        return tuple(self._historical_arcs)

    @property
    def has_arcs(self):
        if self._current_arcs is None:
            return False
        return bool(self._current_arcs)

    def _check_exclusivity(self, new_arc):
        if self._current_arcs is not None:
            for arc in self._current_arcs:
                if not StoryProgressionExclusivity.are_story_progression_arcs_compatible(new_arc, arc):
                    return False
        return True

    def can_add_arc(self, new_arc):
        raise NotImplementedError

    def _can_update_story_progression_tracker(self):
        raise NotImplementedError

    def add_arc(self, new_arc, **kwargs):
        if new_arc.arc_type != self.tracker_type:
            logger.error('Attempting to add arc {} of type {} on tracker of type {}', new_arc, new_arc.arc_type, self.tracker_type)
            return
        arc = new_arc(self)
        result = arc.setup(**kwargs)
        if not result:
            arc.cleanup()
            return result
        if self._current_arcs is None:
            self._current_arcs = []
        self._current_arcs.append(arc)
        return result

    def update_arcs_gen(self, timeline=None):
        if self._current_arcs is None:
            return
        if not self._can_update_story_progression_tracker():
            return
        for arc in tuple(self._current_arcs):
            if is_story_progression_update_archive_enabled():
                gsi_data = GSIStoryProgressionUpdateData()
                if self.tracker_type == StoryType.SIM_BASED:
                    gsi_data.sim_info = self._sim_info
                else:
                    gsi_data.household = self._household
                gsi_data.arc = arc
                gsi_data.chapter = arc._current_chapter
            else:
                gsi_data = None
            (result, updated_chapter) = arc.update_story_arc()
            if gsi_data is not None:
                gsi_data.result = result
                archive_story_progression_update_data(gsi_data)
            arc_ended = False
            if result:
                yield from arc.schedule_drama_nodes_gen(timeline=timeline)
                if result.should_be_made_historical:
                    self._current_arcs.remove(arc)
                    arc_ended = True
                    if self._historical_arcs is None:
                        self._historical_arcs = []
                    self._historical_arcs.append(arc)
            elif result.result_type != StoryProgressionResultType.FAILED_PRECONDITIONS:
                self._current_arcs.remove(arc)
                arc_ended = True
            if arc_ended:
                story_progression_telemetry.send_arc_complete_telemetry(updated_chapter, result.result_type)

    def try_remove_historical_arc(self, arc):
        if self._historical_arcs is not None and arc in self._historical_arcs:
            self._historical_arcs.remove(arc)
            return True
        return False

    def get_random_historical_chapter(self):
        current_historical_arcs = []
        if self._current_arcs is not None:
            for arc in self._current_arcs:
                arc.remove_expired_historical_chapters()
                if arc.historical_chapters:
                    current_historical_arcs.append(arc)
        if self._historical_arcs is not None:
            for arc in tuple(self._historical_arcs):
                arc.remove_expired_historical_chapters()
                if arc.historical_chapters:
                    current_historical_arcs.append(arc)
                else:
                    self._historical_arcs.remove(arc)
            if not self._historical_arcs:
                self._historical_arcs = None
        if not current_historical_arcs:
            return (None, None)
        return random.choice(current_historical_arcs).get_random_historical_chapter()

    def save(self, story_progression_tracker_proto):
        if self._current_arcs is not None:
            for arc in self._current_arcs:
                with ProtocolBufferRollback(story_progression_tracker_proto.current_arcs) as arc_msg:
                    arc.save(arc_msg)
        if self._historical_arcs is not None:
            for arc in self._historical_arcs:
                with ProtocolBufferRollback(story_progression_tracker_proto.historical_arcs) as arc_msg:
                    arc.save(arc_msg)

    def load(self, story_progression_tracker_proto):
        arc_instance_manager = services.get_instance_manager(Types.STORY_ARC)
        for arc_msg in story_progression_tracker_proto.current_arcs:
            arc_type = arc_instance_manager.get(arc_msg.type)
            if arc_type is None:
                pass
            else:
                if self._current_arcs is None:
                    self._current_arcs = []
                arc = arc_type(self)
                arc.load(arc_msg)
                self._current_arcs.append(arc)
        now = services.time_service().sim_now
        expiration_timespan = StoryProgTunables.HISTORY.chapter_history_lifetime()
        for arc_msg in story_progression_tracker_proto.historical_arcs:
            arc_type = arc_instance_manager.get(arc_msg.type)
            if arc_type is None:
                pass
            else:
                for historical_chapter_msg in arc_msg.historical_chapters:
                    if now - DateAndTime(historical_chapter_msg.completion_time) < expiration_timespan:
                        break
                arc = arc_type(self)
                arc.load(arc_msg)
                if self._historical_arcs is None:
                    self._historical_arcs = []
                self._historical_arcs.append(arc)

    def on_zone_load(self):
        if self._current_arcs:
            self.cache_active_arcs()
            for arc in self._current_arcs:
                arc.on_zone_load()
        if self._historical_arcs:
            self.cache_historical_arcs()

    def cache_active_arcs(self):
        raise NotImplementedError

    def cache_historical_arcs(self):
        raise NotImplementedError

class SimStoryProgressionTracker(BaseStoryProgressionTracker, SimInfoTracker):

    def __init__(self, sim_info):
        super().__init__()
        self._sim_info = sim_info

    @constproperty
    def tracker_type():
        return StoryType.SIM_BASED

    @property
    def sim_info(self):
        return self._sim_info

    @property
    def owner_name(self):
        return self._sim_info.full_name

    def _can_update_story_progression_tracker(self):
        if self._sim_info.is_in_travel_group():
            return False
        elif self._sim_info.is_instanced(allow_hidden_flags=ALL_HIDDEN_REASONS):
            return False
        return True

    def can_add_arc(self, new_arc):
        if not self._check_exclusivity(new_arc):
            return False
        elif not self._sim_info.household.story_progression_tracker._check_exclusivity(new_arc):
            return False
        return True

    @property
    def reserved_household_slots(self):
        if self._current_arcs is None:
            return 0
        return sum(arc.reserved_household_slots for arc in self._current_arcs)

    def load(self, story_progression_tracker_proto):
        super().load(story_progression_tracker_proto)
        if self._current_arcs:
            services.get_story_progression_service().cache_active_arcs_sim_id(self._sim_info.id)

    def cache_active_arcs(self):
        services.get_story_progression_service().cache_active_arcs_sim_id(self._sim_info.id)

    def cache_historical_arcs(self):
        services.get_story_progression_service().cache_historical_arcs_sim_id(self._sim_info.id)

class HouseholdStoryProgressionTracker(BaseStoryProgressionTracker, HouseholdTracker):

    def __init__(self, household):
        super().__init__()
        self._household = household

    @constproperty
    def tracker_type():
        return StoryType.HOUSEHOLD_BASED

    @property
    def household(self):
        return self._household

    @property
    def owner_name(self):
        return self._household.name

    def _can_update_story_progression_tracker(self):
        return services.current_zone_id() != self._household.home_zone_id

    def can_add_arc(self, new_arc):
        if not self._check_exclusivity(new_arc):
            return False
        for sim_info in self._household:
            story_progression_tracker = sim_info.story_progression_tracker
            if story_progression_tracker is None:
                pass
            elif not story_progression_tracker._check_exclusivity(new_arc):
                return False
        return True

    def load(self, story_progression_tracker_proto):
        super().load(story_progression_tracker_proto)
        if self._current_arcs:
            services.get_story_progression_service().cache_active_arcs_household_id(self._household.id)

    def cache_active_arcs(self):
        services.get_story_progression_service().cache_active_arcs_household_id(self._household.id)

    def cache_historical_arcs(self):
        services.get_story_progression_service().cache_historical_arcs_household_id(self._household.id)
