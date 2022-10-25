from balloon.balloon_utils import create_balloon_requestfrom balloon.balloon_variant import BalloonVariantfrom event_testing.resolver import SingleSimResolverfrom routing.route_events.route_event_mixins import RouteEventDataBasefrom sims4.tuning.tunable import HasTunableFactory, AutoFactoryInit, TunableList, TunableRangeimport sims4.random
class RouteEventTypeBalloon(RouteEventDataBase, HasTunableFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'balloons': TunableList(description='\n             A list of the possible balloons and balloon categories.\n             ', tunable=BalloonVariant.TunableFactory()), '_duration_override': TunableRange(description='\n            The duration we want this route event to have. This modifies how\n            much of the route time this event will take up to play the\n            animation. For route events that freeze locomotion, you might\n            want to set this to a very low value. Bear in mind that high\n            values are less likely to be scheduled for shorter routes.\n            ', tunable_type=float, default=0, minimum=0)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._balloon_icons = None

    def is_valid_for_scheduling(self, actor, path):
        if not self._balloon_icons:
            return False
        return True

    @property
    def duration_override(self):
        return self._duration_override

    def prepare(self, actor):
        if self._balloon_icons is None:
            self._balloon_icons = []
        resolver = SingleSimResolver(actor)
        balloons = []
        for balloon in self.balloons:
            balloons = balloon.get_balloon_icons(resolver)
            self._balloon_icons.extend(balloons)

    def execute(self, actor, **kwargs):
        pass

    def process(self, actor):
        if not self._balloon_icons:
            return
        balloon = sims4.random.weighted_random_item(self._balloon_icons)
        if balloon is None:
            return
        resolver = SingleSimResolver(actor)
        request = create_balloon_request(balloon, actor, resolver)
        request.distribute()
