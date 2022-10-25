import services
class RegisterWithLostAndFound(HasTunableSingletonFactory, AutoFactoryInit):

    def __call__(self, subject, target):
        lost_and_found_reg_info = target.get_lost_and_found_registration_info()
        if lost_and_found_reg_info is None:
            logger.error('Attempting to register lost and found for an object who has no lost and found registration info. object {}. Loot: {}', target, self, owner='yozhang')
            return
        services.get_object_lost_and_found_service().add_game_object(subject.zone_id, target.id, subject.id, subject.household_id, lost_and_found_reg_info.time_before_lost, lost_and_found_reg_info.return_to_individual_sim)

class UnregisterWithLostAndFound(HasTunableSingletonFactory, AutoFactoryInit):

    def __call__(self, subject, target):
        services.get_object_lost_and_found_service().remove_object(target.id)

class LostAndFoundOp(BaseLootOperation):
    FACTORY_TUNABLES = {'object': TunableEnumEntry(description='\n            The participant that will be interacting with lost and found service.\n            ', tunable_type=ParticipantType, default=ParticipantType.Object), 'operation': TunableVariant(description='\n            This determines the behavior of the lost and found operation.\n            ', register_object=RegisterWithLostAndFound.TunableFactory(), unregister_object=UnregisterWithLostAndFound.TunableFactory(), default='register_object')}

    def __init__(self, object, operation, **kwargs):
        super().__init__(target_participant_type=object, **kwargs)
        self._operation = operation

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if target is None:
            logger.error('Lost and found loot found None object. Participant {}. Loot: {}', self.target_participant_type, self, owner='yozhang')
            return
        if subject is None:
            logger.error('Lost and found loot found None owner sim. Participant {}. Loot: {}', self.subject, self, owner='yozhang')
            return
        self._operation(subject, target)
