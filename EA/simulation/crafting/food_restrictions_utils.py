import servicesimport sims4from sims4.localization import TunableLocalizedStringFactoryfrom sims4.tuning.dynamic_enum import DynamicEnumfrom sims4.tuning.tunable import TunableReference, TunableEnumEntry, TunableMappinglogger = sims4.log.Logger('Food Restrictions')
class FoodRestrictionUtils:

    class FoodRestrictionEnum(DynamicEnum):
        INVALID = 0
