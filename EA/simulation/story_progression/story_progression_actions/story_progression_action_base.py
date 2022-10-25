import servicesfrom abc import ABCfrom interactions import ParticipantTypeSavedStoryProgressionStringfrom sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, OptionalTunable, TunableEnumEntryfrom story_progression.story_progression_result import StoryProgressionResult, StoryProgressionResultType
class BaseStoryProgressionAction(HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'store_world_name_participant': OptionalTunable(description='\n            If enabled we will store off the target world name into the specified participant type for future use in tokens\n            or other resolvers.\n            ', tunable=TunableEnumEntry(tunable_type=ParticipantTypeSavedStoryProgressionString, default=ParticipantTypeSavedStoryProgressionString.SavedStoryProgressionString1)), 'store_household_name_participant': OptionalTunable(description='\n            If enabled we will store off the affected household name for future use in tokens or other resolvers.\n            ', tunable=TunableEnumEntry(tunable_type=ParticipantTypeSavedStoryProgressionString, default=ParticipantTypeSavedStoryProgressionString.SavedStoryProgressionString1))}

    def __init__(self, owner_arc, **kwargs):
        super().__init__(**kwargs)
        self._owner_arc = owner_arc

    def setup_story_progression_action(self, **kwargs):
        return StoryProgressionResult(StoryProgressionResultType.SUCCESS)

    def run_story_progression_action(self):
        result = self._run_story_progression_action()
        if result:
            self._save_participants()
        return result

    @property
    def target_zone_id(self):
        return self.affected_household.home_zone_id

    @property
    def affected_household(self):
        raise NotImplementedError

    def _run_story_progression_action(self):
        raise NotImplementedError

    def _save_participants(self):
        target_zone_id = self.target_zone_id
        if target_zone_id is not None and self.store_world_name_participant is not None:
            neighborhood_proto = services.get_persistence_service().get_neighborhood_proto_buf_from_zone_id(target_zone_id)
            if neighborhood_proto is not None:
                self._owner_arc.store_participant(self.store_world_name_participant, neighborhood_proto.name)
        affected_household = self.affected_household
        if affected_household is not None and self.store_household_name_participant is not None:
            self._owner_arc.store_participant(self.store_household_name_participant, affected_household.name)

    def get_gsi_data(self):
        pass

    def save_custom_data(self, writer):
        pass

    def load_custom_data(self, reader):
        pass

class BaseSimStoryProgressionAction(BaseStoryProgressionAction, ABC):

    @property
    def affected_household(self):
        return self._owner_arc.sim_info.household

    @property
    def reserved_household_slots(self):
        return 0

class BaseHouseholdStoryProgressionAction(BaseStoryProgressionAction, ABC):

    @property
    def affected_household(self):
        return self._owner_arc.household
