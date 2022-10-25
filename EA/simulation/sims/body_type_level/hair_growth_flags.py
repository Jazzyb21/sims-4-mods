import enumfrom sims.outfits.outfit_enums import BodyType
class HairGrowthFlags(enum.IntFlags, export=False):
    NONE = 0
    FACIAL_HAIR = 256
    ARM_HAIR = 512
    LEG_HAIR = 1024
    TORSOFRONT_HAIR = 2048
    TORSOBACK_HAIR = 4096
    ALL = FACIAL_HAIR | ARM_HAIR | LEG_HAIR | TORSOFRONT_HAIR | TORSOBACK_HAIR
HAIR_GROWTH_TO_BODY_TYPE = {HairGrowthFlags.TORSOBACK_HAIR: BodyType.BODYHAIR_TORSOBACK, HairGrowthFlags.TORSOFRONT_HAIR: BodyType.BODYHAIR_TORSOFRONT, HairGrowthFlags.LEG_HAIR: BodyType.BODYHAIR_LEG, HairGrowthFlags.ARM_HAIR: BodyType.BODYHAIR_ARM, HairGrowthFlags.FACIAL_HAIR: BodyType.FACIAL_HAIR, HairGrowthFlags.NONE: BodyType.NONE}