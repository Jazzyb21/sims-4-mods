import enum
class SimRelBitShift(enum.Int, export=False):
    SIMRELEBITSHIFT_MOTHER = 0
    SIMRELEBITSHIFT_FATHER = 1
    SIMRELEBITSHIFT_DAUGHTER = 2
    SIMRELEBITSHIFT_SON = 3
    SIMRELEBITSHIFT_WIFE = 4
    SIMRELEBITSHIFT_HUSBAND = 5
    SIMRELEBITSHIFT_FIANCEE = 6
    SIMRELEBITSHIFT_FIANCE = 7
    SIMRELEBITSHIFT_MAX = 7
    SIMRELEBITSHIFT_PREEXISTING = 31

class SimRelBitFlags(enum.IntFlags, export=False):
    SIMRELBITFLAG_NONE = 0
    SIMRELBITFLAG_MOTHER = 1 << SimRelBitShift.SIMRELEBITSHIFT_MOTHER
    SIMRELBITFLAG_FATHER = 1 << SimRelBitShift.SIMRELEBITSHIFT_FATHER
    SIMRELBITFLAG_DAUGHTER = 1 << SimRelBitShift.SIMRELEBITSHIFT_DAUGHTER
    SIMRELBITFLAG_SON = 1 << SimRelBitShift.SIMRELEBITSHIFT_SON
    SIMRELBITFLAG_WIFE = 1 << SimRelBitShift.SIMRELEBITSHIFT_WIFE
    SIMRELBITFLAG_HUSBAND = 1 << SimRelBitShift.SIMRELEBITSHIFT_HUSBAND
    SIMRELBITFLAG_FIANCEE = 1 << SimRelBitShift.SIMRELEBITSHIFT_FIANCEE
    SIMRELBITFLAG_FIANCE = 1 << SimRelBitShift.SIMRELEBITSHIFT_FIANCE
    SIMRELBITFLAG_PREEXISTING = 1 << SimRelBitShift.SIMRELEBITSHIFT_PREEXISTING
    SIMRELBITS_MALE = SIMRELBITFLAG_FATHER | SIMRELBITFLAG_SON | SIMRELBITFLAG_HUSBAND | SIMRELBITFLAG_FIANCE
    SIMRELBITS_FEMALE = SIMRELBITFLAG_MOTHER | SIMRELBITFLAG_DAUGHTER | SIMRELBITFLAG_WIFE | SIMRELBITFLAG_FIANCEE
    SIMRELBITS_CHILD = SIMRELBITFLAG_DAUGHTER | SIMRELBITFLAG_SON
    SIMRELBITS_PARENT = SIMRELBITFLAG_MOTHER | SIMRELBITFLAG_FATHER
    SIMRELBITS_SPOUSE = SIMRELBITFLAG_WIFE | SIMRELBITFLAG_HUSBAND
    SIMRELBITS_FIANCE = SIMRELBITFLAG_FIANCE | SIMRELBITFLAG_FIANCEE
    SIMRELBITS_ALL = SIMRELBITS_CHILD | SIMRELBITS_PARENT | SIMRELBITS_SPOUSE | SIMRELBITS_FIANCE
