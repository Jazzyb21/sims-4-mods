from event_testing.results import TestResult, TestResultNumericfrom event_testing.test_events import TestEventfrom caches import cached_testfrom interactions import ParticipantTypefrom sims.unlock_tracker import TunableUnlockVariantfrom sims4.tuning.tunable import TunableFactory, TunableEnumEntry, Tunable, TunableThreshold, HasTunableSingletonFactory, AutoFactoryInit, TunableEnumWithFilterfrom sims4.tuning.tunable_base import EnumBinaryExportTypefrom tag import Tagimport event_testing.test_baseimport sims4.tuning.tunablelogger = sims4.log.Logger('Unlock Tracker Tests')
class UnlockTrackerTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):

    @TunableFactory.factory_option
    def participant_type_override(participant_type_enum, participant_type_default):
        return {'subject': TunableEnumEntry(description='\n                    Who or what to apply this test to\n                    ', tunable_type=participant_type_enum, default=participant_type_default)}

    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            Who or what to apply this test to\n            ', tunable_type=ParticipantType, default=ParticipantType.Actor), 'unlock_item': TunableUnlockVariant(description='\n            The unlock item that Sim has or not.\n            '), 'invert': Tunable(description='\n            If checked, test will pass if any subject does NOT have the unlock.\n            ', tunable_type=bool, default=False)}

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=()):
        reason = 'There are no targets to test!' if not test_targets else None
        for target in test_targets:
            if not target.is_sim:
                reason = 'Cannot test unlock on non-Sim object {} as subject {}.'.format(target, self.subject)
            elif target.unlock_tracker is None or not target.unlock_tracker.is_unlocked(self.unlock_item):
                reason = "Sim {} hasn't unlocked {}.".format(target, self.unlock_item)
            elif not self.invert:
                return TestResult.TRUE
        if self.invert and test_targets:
            if reason is None:
                reason = 'No subjects have {} locked'.format(self.unlock_item)
            else:
                return TestResult.TRUE
        return TestResult(False, reason, tooltip=self.tooltip)

class UnlockTrackerAmountTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    test_events = (TestEvent.UnlockTrackerItemUnlocked,)
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            Who or what to apply this test to\n            ', tunable_type=ParticipantType, default=ParticipantType.Actor), 'test_tag': TunableEnumWithFilter(description='\n            This test will look how many items with this tag have been unlocked.\n            ', tunable_type=Tag, filter_prefixes=('recipe', 'spell'), default=Tag.INVALID, invalid_enums=(Tag.INVALID,), pack_safe=True, binary_type=EnumBinaryExportType.EnumUint32), 'threshold': TunableThreshold(description='\n            The required number of specified things required to pass the test.\n            ')}

    def get_expected_args(self):
        return {'test_targets': self.subject}

    @cached_test
    def __call__(self, test_targets=()):
        for target in test_targets:
            if not target.is_sim:
                return TestResult(False, 'Cannot test unlock on none_sim object {} as subject {}.', target, self.subject, tooltip=self.tooltip)
            if target.unlock_tracker is None:
                return TestResult(False, 'Sim {} does not have an unlock tracker.', target, tooltip=self.tooltip)
            number_unlocked = target.unlock_tracker.get_number_unlocked(self.test_tag)
            if not self.threshold.compare(number_unlocked):
                return TestResultNumeric(False, "Sim {} hasn't unlocked the required amount of {}.", target, self.test_tag, current_value=number_unlocked, goal_value=self.threshold.value, tooltip=self.tooltip)
        return TestResult.TRUE

    def goal_value(self):
        return self.threshold.value
