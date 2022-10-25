import enum
class GuidanceTipPlatformFilter(enum.Int):
    ALL_PLATFORMS = 0
    DESKTOP_ONLY = 1
    CONSOLE_ONLY = 2

class GuidanceTipGameState(enum.Int):
    GAMESTATE_NONE = 0
    LIVE_MODE = 270579719
    BUILD_BUY = 2919482169
    CAS = 983016380
    NEIGHBORHOOD_VIEW = 3640749201
    GALLERY = 1
    TRAVEL = 238138433
    MAIN_MENU = 1273744144

class GuidanceTipGroupConditionType(enum.Int):
    AND = 0
    OR = 1

class GuidanceTipRuleBoolen(enum.Int):
    NEVER = 0
    ALWAYS = 1

class GuidanceTipMode(enum.Int):
    DISABLED = 0
    STANDARD = 1

class GuidanceTipOptionType(enum.Int):
    STANDARD = 0
    EXPANDED = 1
