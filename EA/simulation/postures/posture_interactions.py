from animation.posture_manifest import Hand
class HoldObjectBase(SuperInteraction):

    @classmethod
    def potential_interactions(cls, target, context, **kwargs):
        yield interactions.aop.AffordanceObjectPair(cls, target, cls, None, hand=Hand.LEFT, **kwargs)
        yield interactions.aop.AffordanceObjectPair(cls, target, cls, None, hand=Hand.RIGHT, **kwargs)

class HoldObject(HoldObjectBase):
    INSTANCE_TUNABLES = {'_carry_posture_type': TunableReference(manager=services.get_instance_manager(sims4.resources.Types.POSTURE), description='The carry posture type for this version of HoldObject.')}

    @classmethod
    def get_provided_posture_change(cls, aop):
        return postures.posture_specs.PostureOperation.PickUpObject(cls._carry_posture_type, aop.target)

    @classproperty
    def provided_posture_type(cls):
        return cls._carry_posture_type

class HoldNothing(HoldObjectBase):

    @classmethod
    def get_provided_posture_change(cls, aop):
        return postures.posture_specs.PostureOperation.PickUpObject(CarryPostureStaticTuning.POSTURE_CARRY_NOTHING, None)

    @classproperty
    def provided_posture_type(cls):
        return CarryPostureStaticTuning.POSTURE_CARRY_NOTHING
