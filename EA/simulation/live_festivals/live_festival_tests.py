import event_testing.test_baseimport servicesimport sims4from live_events.live_event_service import LiveEventTypefrom event_testing.results import TestResultfrom live_festivals import live_festival_tuningfrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableVariant, TunableTuple, Tunablefrom world import get_lot_id_from_instance_idlogger = sims4.log.Logger('Live Festival Tests', default_owner='asantos')
class ActiveLiveFestivalTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    TEST_TYPE_OPEN_BUSINESS = 0
    FACTORY_TUNABLES = {'test_type': TunableVariant(description='\n            What you want to check about the active live event.\n            ', open_business_in_location=TunableTuple(description='\n                Check if there is any business open in the location of an active festival.\n                ', locked_args={'test_type': TEST_TYPE_OPEN_BUSINESS}), default='open_business_in_location'), 'negate': Tunable(description='\n            If checked then the result of the test will be negated.\n            ', tunable_type=bool, default=False)}

    def get_expected_args(self):
        return {}

    def __call__(self, *args, **kwargs):
        live_event_service = services.get_live_event_service()
        if live_event_service is None:
            return TestResult(False, 'There is no active Live Event service.', tooltip=self.tooltip)
        active_unique_festival = live_event_service.get_current_unique_live_event_of_type(LiveEventType.LIVE_FESTIVAL)
        if active_unique_festival is None:
            if self.negate:
                return TestResult.TRUE
            return TestResult(False, 'There is no active unique live festival.', tooltip=self.tooltip)
        if self.test_type.test_type == self.TEST_TYPE_OPEN_BUSINESS:
            if active_unique_festival not in live_festival_tuning.LiveFestivalTuning.LIVE_FESTIVAL_EVENT_DATA:
                logger.error('Trying to run ActiveLiveFestivalTest, but festival {} does not have its tuning set in LiveFestivalTuning.', active_unique_festival, owner='asantos')
                return TestResult(False, 'Missing tuning for festival {}.', active_unique_festival, tooltip=self.tooltip)
            festival_tuning = live_festival_tuning.LiveFestivalTuning.LIVE_FESTIVAL_EVENT_DATA[active_unique_festival]
            festival_lot_id = get_lot_id_from_instance_id(festival_tuning.lot)
            zone_id = services.get_persistence_service().resolve_lot_id_into_zone_id(festival_lot_id, ignore_neighborhood_id=True)
            business_manager = services.business_service().get_business_manager_for_zone(zone_id=zone_id)
            is_open_business = business_manager.is_open if business_manager is not None else False
            if not is_open_business:
                if self.negate:
                    return TestResult.TRUE
                return TestResult(False, 'There are no open businesses at the location of the live event {}.', active_unique_festival, tooltip=self.tooltip)
        if self.negate:
            return TestResult(False, 'The Active live event test for {} passed, but this test is negated.', active_unique_festival, tooltip=self.tooltip)
        return TestResult.TRUE
