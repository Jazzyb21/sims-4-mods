import enum
class StoryProgressionFlags(enum.IntFlags, export=False):
    DISABLED = 0
    ALLOW_POPULATION_ACTION = 1
    ALLOW_INITIAL_POPULATION = 2
    SIM_INFO_FIREMETER = 4

class StoryProgressionArcSeedReason(enum.Int, export=False):
    SYSTEM = 0
    LOOT = 1
