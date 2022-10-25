from traits.trait_type import TraitTypeimport enum
class PreferenceTypes(enum.Int):
    LIKE = TraitType.LIKE
    DISLIKE = TraitType.DISLIKE

class PreferenceSubject(enum.Int):
    OBJECT = 0
    DECOR = 1
