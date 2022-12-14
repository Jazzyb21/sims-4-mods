from interactions.base.super_interaction import SuperInteractionfrom sims4.tuning.tunable import TunableReferenceimport servicesimport sims4.resources
class StandSuperInteraction(SuperInteraction):
    STAND_POSTURE_TYPE = TunableReference(manager=services.get_instance_manager(sims4.resources.Types.POSTURE), description='The Posture Type for the Stand posture.')

    @classmethod
    def _is_linked_to(cls, super_affordance):
        return cls is not super_affordance

    def get_cancel_replacement_aops_contexts_postures(self, can_transfer_ownership=True, carry_cancel_override=None):
        if self.target is None and self.sim.posture.posture_type == self.STAND_POSTURE_TYPE:
            return []
        return super().get_cancel_replacement_aops_contexts_postures(can_transfer_ownership=can_transfer_ownership, carry_cancel_override=carry_cancel_override)
