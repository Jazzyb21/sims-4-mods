import random
class _BarflySituationState(SituationState):
    pass

class BarflySituation(SituationComplexCommon):
    INSTANCE_TUNABLES = {'barfly_job_and_role': TunableSituationJobAndRoleState(description='\n            The job and role of the barfly.\n            '), 'starting_entitlement': OptionalTunable(description='\n            If enabled, this situation is locked by an entitlement. Otherwise,\n            this situation is available to all players.\n            ', tunable=TunableEnumEntry(description='\n                Pack required for this event to start.\n                ', tunable_type=Pack, default=Pack.BASE_GAME))}
    REMOVE_INSTANCE_TUNABLES = Situation.NON_USER_FACING_REMOVE_INSTANCE_TUNABLES

    @classmethod
    def _states(cls):
        return (SituationStateData(1, _BarflySituationState),)

    @classmethod
    def _get_tuned_job_and_default_role_state_tuples(cls):
        return [(cls.barfly_job_and_role.job, cls.barfly_job_and_role.role_state)]

    @classmethod
    def default_job(cls):
        pass

    @classmethod
    def situation_meets_starting_requirements(cls, **kwargs):
        if cls.starting_entitlement is None:
            return True
        return is_available_pack(cls.starting_entitlement)

    def start_situation(self):
        super().start_situation()
        self._change_state(_BarflySituationState())
