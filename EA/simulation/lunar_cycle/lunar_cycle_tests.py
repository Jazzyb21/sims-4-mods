import servicesfrom event_testing.results import TestResultfrom event_testing.test_base import BaseTestfrom lunar_cycle.lunar_cycle_enums import LunarPhaseTypefrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntryfrom singletons import EMPTY_DICTfrom tunable_utils.tunable_white_black_list import TunableWhiteBlackList
class LunarPhaseTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):
    FACTORY_TUNABLES = {'phases_to_check': TunableWhiteBlackList(description='\n            Whitelist or blacklist of phases to check against.  When untuned, all phases are valid.\n            ', tunable=TunableEnumEntry(description='\n                The lunar phase to test against.\n                ', tunable_type=LunarPhaseType, default=LunarPhaseType.NEW_MOON))}

    @staticmethod
    def get_expected_args():
        return EMPTY_DICT

    def __call__(self):
        lunar_cycle_service = services.lunar_cycle_service()
        current_phase = lunar_cycle_service.current_phase
        if not self.phases_to_check.test_item(current_phase):
            return TestResult(False, '{} is in blacklist or missing from whitelist', current_phase, tooltip=self.tooltip)
        return TestResult.TRUE
