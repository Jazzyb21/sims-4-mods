import enum
class ConditionalLayerRequestSpeedType(enum.Int, export=False):
    GRADUALLY = ...
    IMMEDIATELY = ...

class ConditionalLayerRequestType(enum.Int, export=False):
    LOAD_LAYER = ...
    DESTROY_LAYER = ...
