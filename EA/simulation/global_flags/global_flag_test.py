import servicesfrom event_testing.results import TestResultfrom event_testing.test_base import BaseTestfrom global_flags.global_flags import GlobalFlagsfrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumFlags, Tunable
class GlobalFlagTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'flags': TunableEnumFlags(description='\n            The flags to check against being set in\n            the global flag service.\n            ', enum_type=GlobalFlags), 'negate': Tunable(description='\n            If enabled then we will check if any of the flags\n            are not set.\n            ', tunable_type=bool, default=False)}

    def get_expected_args(self):
        return {}

    def __call__(self):
        if services.global_flag_service().has_any_flag(self.flags):
            if self.negate:
                return TestResult(False, 'At least one of flags {} is set.', self.flags)
            return TestResult.TRUE
        elif self.negate:
            return TestResult.TRUE
        else:
            return TestResult(False, 'None of flags {} are set.', self.flags)
