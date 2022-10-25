from caches import cached_testfrom event_testing.results import TestResultfrom event_testing.test_base import BaseTestfrom interactions import ParticipantTypeObjectfrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableVariant, TunableEnumEntry, Tunable
class FishingTest(HasTunableSingletonFactory, AutoFactoryInit, BaseTest):

    class _HasFish(HasTunableSingletonFactory):

        def __call__(self, target, tooltip=None):
            fishing_location_component = target.fishing_location_component
            if fishing_location_component is None:
                return TestResult(False, 'Target {} has no fishing location component.', target, tooltip=tooltip)
            fishing_data = fishing_location_component.fishing_data
            if not any(fishing_data.get_possible_fish_gen()):
                return TestResult(False, 'Target {} has no fish.', target, tooltip=tooltip)
            return TestResult.TRUE

    FACTORY_TUNABLES = {'test': TunableVariant(description='\n            The test to run.\n            ', has_fish=_HasFish.TunableFactory(), default='has_fish'), 'target': TunableEnumEntry(description='\n            The target to test against.\n            ', tunable_type=ParticipantTypeObject, default=ParticipantTypeObject.Object), 'negate': Tunable(description='\n            If checked, the test will be negated. \n            ', tunable_type=bool, default=False)}

    def get_expected_args(self):
        return {'targets': self.target}

    @cached_test
    def __call__(self, targets=None):
        target = next(iter(targets), None)
        if target is None:
            return TestResult(False, 'Target is none', tooltip=self.tooltip)
        result = self.test(target, tooltip=self.tooltip)
        if self.negate:
            if result:
                return TestResult(False, 'Test passed but negate is checked', tooltip=self.tooltip)
            else:
                return TestResult.TRUE
        return result
