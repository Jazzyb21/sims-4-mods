from live_events.live_event_service import LiveEventState, LiveEventNamefrom event_testing.results import TestResultfrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, Tunable, TunableEnumEntryimport event_testing.test_baseimport services
class LiveEventStateTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    FACTORY_TUNABLES = {'live_event_name': TunableEnumEntry(description='\n            The name of the live event we are checking.\n            ', tunable_type=LiveEventName, default=LiveEventName.DEFAULT, invalid_enums=(LiveEventName.DEFAULT,)), 'state': TunableEnumEntry(description='\n            If the live event is in this state, this test passes.\n            ', tunable_type=LiveEventState, default=LiveEventState.ACTIVE), 'negate': Tunable(description='\n            If checked then the result of the test will be negated.\n            ', tunable_type=bool, default=False)}

    def get_expected_args(self):
        return {}

    def __call__(self, *args, **kwargs):
        live_event_service = services.get_live_event_service()
        if live_event_service is None:
            return TestResult(False, 'There is no active Live Event service.', tooltip=self.tooltip)
        live_event_state = live_event_service.get_live_event_state(self.live_event_name)
        if live_event_state != self.state:
            if self.negate:
                return TestResult.TRUE
            return TestResult(False, 'The live event {} is in {} state, not {}.', self.live_event_name.name, live_event_state, self.state, tooltip=self.tooltip)
        if self.negate:
            return TestResult(False, 'The live event {} is in {} state, but this test is negated.', self.live_event_name.name, live_event_state, tooltip=self.tooltip)
        return TestResult.TRUE
