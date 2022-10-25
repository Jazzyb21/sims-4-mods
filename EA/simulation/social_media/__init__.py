import enum
class SocialMediaNarrative(enum.Int):
    FRIENDLY = 0
    FLIRTY = 1
    MEAN = 2
    PROUD = 3
    EMBARRASSED = 4
    EXCITED = 5
    HAPPY = 6
    SAD = 7
    STRESSED = 8
    FUNNY = 9
    UNCOMFORTABLE = 10
    PRANK = 11

class SocialMediaPostType(enum.Int):
    DEFAULT = 0
    DIRECT_MESSAGE = 1
    FRIEND_REQUEST = 2
    FOLLOWERS_UPDATE = 3
    PUBLIC_POST = 4

class SocialMediaPolarity(enum.Int):
    POSITIVE = 0
    NEGATIVE = 1
