import enum
class LunarPhaseType(enum.Int):
    NEW_MOON = 0
    WAXING_CRESCENT = 1
    FIRST_QUARTER = 2
    WAXING_GIBBOUS = 3
    FULL_MOON = 4
    WANING_GIBBOUS = 5
    THIRD_QUARTER = 6
    WANING_CRESCENT = 7

class LunarPhaseLockedOption(LunarPhaseType, export=False):
    NO_LUNAR_PHASE_LOCK = 8

class LunarCycleLengthOption(enum.Int):
    TWO_DAY = 0
    FOUR_DAY = 1
    FULL_LENGTH = 2
    DOUBLE_LENGTH = 3
    TRIPLE_LENGTH = 4
