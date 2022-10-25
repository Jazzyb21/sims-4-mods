from event_testing.tests import TestListLoadingMixin
class TunablePieMenuColorTestVariant(TunableVariant):

    def __init__(self, **kwargs):
        tunables = {'mood': MoodTest.TunableFactory()}
        kwargs.update(tunables)
        super().__init__(**kwargs)

class PieMenuColorTestList(event_testing.tests.TestListLoadingMixin):
    DEFAULT_LIST = event_testing.tests.TestList()

    def __init__(self, description=None):
        super().__init__(description=description, tunable=TunablePieMenuColorTestVariant())
