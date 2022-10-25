from protocolbuffers import Consts_pb2, UI_pb2, DistributorOps_pb2
class BaseGameLootOperation(BaseLootOperation):
    FACTORY_TUNABLES = {'locked_args': {'advertise': False}}

class LifeExtensionLootOp(BaseLootOperation):

    class RestoreDaysFromAgingProgress(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'days_to_restore': TunableRange(tunable_type=int, default=0, minimum=0)}

        def perform(self, subject, *_, **__):
            subject.decrement_age_progress(self.days_to_restore)

    class ResetAgingProgressInCategory(HasTunableSingletonFactory, AutoFactoryInit):

        def perform(self, subject, *_, **__):
            subject.reset_age_progress()

    class AddDaysToAgingProgress(HasTunableSingletonFactory, AutoFactoryInit):
        FACTORY_TUNABLES = {'days_to_add': TunableRange(tunable_type=int, default=0, minimum=0)}

        def perform(self, subject, *_, **__):
            subject.increment_age_progress(self.days_to_add)

    class FillAgingProgressInCategory(HasTunableSingletonFactory, AutoFactoryInit):

        def perform(self, subject, *_, **__):
            subject.fill_age_progress()

    FACTORY_TUNABLES = {'bonus_days': TunableRange(description="\n            Number of bonus days to be granted to the target's life.\n            ", tunable_type=int, default=1, minimum=0), 'modify_aging_progress': TunableVariant(description='\n            If enabled, this loot will modify aging progress of a sim.\n            ', restore_days_from_aging_progress=RestoreDaysFromAgingProgress.TunableFactory(), reset_aging_progress_in_category=ResetAgingProgressInCategory.TunableFactory(), add_days_to_aging_progress=AddDaysToAgingProgress.TunableFactory(), fill_aging_progress_in_category=FillAgingProgressInCategory.TunableFactory(), locked_args={'disabled': None}, default='disabled')}

    def __init__(self, bonus_days, modify_aging_progress, **kwargs):
        super().__init__(**kwargs)
        self.bonus_days = bonus_days
        self.modify_aging_progress = modify_aging_progress

    @property
    def loot_type(self):
        return LootType.LIFE_EXTENSION

    def _apply_to_subject_and_target(self, subject, target, resolver):
        subject.add_bonus_days(self.bonus_days)
        if self.modify_aging_progress is not None:
            self.modify_aging_progress.perform(subject)

class StateChangeLootOp(BaseLootOperation):
    FACTORY_TUNABLES = {'description': '\n            This loot will change the state of the subject.\n            ', 'state_value': TunableStateValueReference(), 'force_update': Tunable(description="\n            If checked, force update the subject's state.\n            ", tunable_type=bool, default=False)}

    @TunableFactory.factory_option
    def subject_participant_type_options(**kwargs):
        return {'subject': TunableVariant(description='\n            The subject of this loot.\n            ', participant=TunableEnumEntry(description='"\n                The participant type for the subject of this loot.\n                ', tunable_type=ParticipantType, default=ParticipantType.Actor, invalid_enums=(ParticipantType.Invalid,)), all_objects_with_tag=TunableEnumEntry(description='\n                All objects with this tag.\n                ', tunable_type=tag.Tag, default=tag.Tag.INVALID, invalid_enums=(tag.Tag.INVALID,)), default='participant')}

    def __init__(self, state_value, force_update, **kwargs):
        super().__init__(**kwargs)
        self.state_value = state_value
        self.force_update = force_update

    def _apply_to_subject_and_target(self, subject, target, resolver):
        subject_obj = self._get_object_from_recipient(subject)
        if subject_obj is not None:
            state_value = self.state_value
            subject_obj.set_state(state_value.state, state_value, force_update=self.force_update)

class DialogLootOp(BaseLootOperation):
    FACTORY_TUNABLES = {'dialog': TunableVariant(description='\n            Type of dialog to show.\n            ', notification=UiDialogNotification.TunableFactory(description='\n                This text will display in a notification pop up when completed.\n                '), dialog_ok=UiDialogOk.TunableFactory(description='\n                Display a dialog with an okay button.\n                '), aspiration_progress=UiDialogAspirationProgress.TunableFactory(description="\n                Display a dialog that will show the Sim's progress towards one\n                or more aspirations.\n                "), reveal_sequence=UiDialogRevealSequence.TunableFactory(description="\n                Display a dialog that will show the Sim's gig photos in a sequence.\n                "), npc_display=UiDialogNpcDisplay.TunableFactory(description='\n                Display a dialog that will show a list of Sims and information\n                about them in a grid.\n                '), story_progression_discovery_notification=UIDialogNotificationStoryProgressionDiscovery.TunableFactory(description='\n                Display a dialog that displays text informing the player of a recently completed story progression\n                chapter. \n                ', locked_args={'text': None}), default='notification')}

    def __init__(self, dialog, **kwargs):
        super().__init__(**kwargs)
        self.dialog = dialog

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if not services.current_zone().is_zone_loading:
            owner = subject if subject.is_sim else services.get_active_sim()
            if owner is not None and owner.is_selectable:
                dialog = self.dialog(owner, resolver)
                dialog.show_dialog(event_id=self.dialog.factory.DIALOG_MSG_TYPE)
