import services
class _ArtistEnterState(CommonInteractionCompletedSituationState):

    def _on_interaction_of_interest_complete(self, **kwargs):
        self._change_state(self.owner.artist_perform_state())

    def timer_expired(self):
        self._change_state(self.owner.artist_perform_state())

class _ArtistPerformState(CommonInteractionCompletedSituationState):

    def _on_interaction_of_interest_complete(self, **kwargs):
        self._change_state(self.owner.artist_exit_state())

    def timer_expired(self):
        self._change_state(self.owner.artist_exit_state())

class _ArtistExitState(CommonInteractionCompletedSituationState):

    def _on_interaction_of_interest_complete(self, **kwargs):
        self.owner._self_destruct()

    def timer_expired(self):
        self.owner._self_destruct()

class MusicPerformanceSituation(BaseGenericFestivalSituation):
    INSTANCE_TUNABLES = {'artist_enter_state': _ArtistEnterState.TunableFactory(description='\n            The state where the artist routes to stage.\n            ', display_name='1. Artist Enter State', tuning_group=SituationComplexCommon.SITUATION_STATE_GROUP), 'artist_perform_state': _ArtistPerformState.TunableFactory(description='\n            The state where the artist performs a song.\n            ', display_name='2. Artist Perform State', tuning_group=SituationComplexCommon.SITUATION_STATE_GROUP), 'artist_exit_state': _ArtistExitState.TunableFactory(description='\n            The state where the artist exits the stage and despawns.\n            ', display_name='3. Artist Exit State', tuning_group=SituationComplexCommon.SITUATION_STATE_GROUP), 'artist_job_and_role': TunableSituationJobAndRoleState(description='\n            The job and role of the performer sim.\n            '), 'audience_member_job_and_role': TunableSituationJobAndRoleState(description='\n            The job and role of an audience member sim.\n            ')}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def start_situation(self):
        super().start_situation()
        self._change_state(self.artist_enter_state())

    def _on_add_sim_to_situation(self, sim, job_type, role_state_type_override=None):
        super()._on_add_sim_to_situation(sim, job_type, role_state_type_override)
        if job_type is self.artist_job_and_role.job:
            culling_service = services.get_culling_service()
            culling_service.set_sim_as_ready_to_be_culled(sim)

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return [(cls.artist_job_and_role.job, cls.artist_job_and_role.role_state), (cls.audience_member_job_and_role.job, cls.audience_member_job_and_role.role_state)]

    @classmethod
    def default_job(cls):
        return cls.audience_member_job_and_role.job

    def _issue_requests(self, spawn_point_override=None):
        super()._issue_requests(spawn_point_override=spawn_point_override)
        request = BouncerRequestFactory(self, callback_data=_RequestUserData(role_state_type=self.audience_member_job_and_role.role_state), job_type=self.audience_member_job_and_role.job, request_priority=BouncerRequestPriority.BACKGROUND_HIGH, user_facing=False, exclusivity=BouncerExclusivityCategory.FESTIVAL_GOER_SNATCHER)
        self.manager.bouncer.submit_request(request)

    @classmethod
    def _states(cls):
        return (SituationStateData(1, _ArtistEnterState, factory=cls.artist_enter_state), SituationStateData(2, _ArtistPerformState, factory=cls.artist_perform_state), SituationStateData(3, _ArtistExitState, factory=cls.artist_exit_state))

class GenericOneStateMusicPerformanceSituation(GenericOneStateFestivalAttendeeSituation):
    INSTANCE_TUNABLES = {'job_and_role': TunableSituationJobAndRoleState(description='\n            The default job and role.\n            ')}

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return [(cls.job_and_role.job, cls.job_and_role.role_state)]

    @classmethod
    def default_job(cls):
        return cls.job_and_role.job

    def _issue_requests(self, spawn_point_override=None):
        super()._issue_requests(spawn_point_override=spawn_point_override)
        request = BouncerRequestFactory(self, callback_data=_RequestUserData(role_state_type=self.job_and_role.role_state), job_type=self.job_and_role.job, request_priority=BouncerRequestPriority.BACKGROUND_HIGH, user_facing=False, exclusivity=BouncerExclusivityCategory.FESTIVAL_GOER_SNATCHER)
        self.manager.bouncer.submit_request(request)
