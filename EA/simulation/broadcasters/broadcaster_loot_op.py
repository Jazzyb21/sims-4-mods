from broadcasters.broadcaster_request import BroadcasterRequest
def verify_immediate_broadcaster(instance_class, tunable_name, source, broadcaster_types=[], **kwargs):
    from broadcasters.broadcaster import Broadcaster
    for tested_broadcaster_tuple in broadcaster_types:
        broadcaster = tested_broadcaster_tuple.item
        if not broadcaster.frequency.frequency_type != Broadcaster.FREQUENCY_ENTER:
            if not broadcaster.immediate:
                logger.error('Only on-enter immediate broadcasters are allowed in this op found {}', broadcaster)
        logger.error('Only on-enter immediate broadcasters are allowed in this op found {}', broadcaster)

class BroadcasterOneShotLootOp(BaseLootOperation):
    FACTORY_TUNABLES = {'broadcaster_request': BroadcasterRequest.TunableFactory(description='\n            The broadcaster request to run.\n            ', verify_tunable_callback=verify_immediate_broadcaster, locked_args={'offset_time': None, 'participant': ParticipantType.Object})}

    def __init__(self, *args, broadcaster_request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.broadcaster_request = broadcaster_request

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject.is_sim and subject.sim_info is subject:
            subject = subject.get_sim_instance()
            if subject is None:
                logger.error('Requested broadcaster for uninstanced Sim')
                return
        request = self.broadcaster_request(subject, sequence=(element_utils.sleep_until_next_tick_element(),))
        if resolver.interaction is not None:
            request.cache_excluded_participants(resolver.interaction)
        sim_timeline = services.time_service().sim_timeline
        sim_timeline.schedule(request)
