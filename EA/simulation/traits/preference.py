from cas.cas_preference_item import ObjectPreferenceItem, CasPreferenceItemfrom objects.object_tests import ObjectTagFactoryfrom sims4.tuning.tunable import Tunable, TunableList, TunableReferencefrom sims4.tuning.tunable_base import GroupNames, ExportModesfrom sims4.utils import classproperty, constpropertyfrom traits.preference_enums import PreferenceSubjectfrom traits.preference_tuning import PreferenceTuningfrom traits.traits import Traitimport sims4import sims4.logimport serviceslogger = sims4.log.Logger('Trait', default_owner='micfisher')
class Preference(Trait):
    INSTANCE_TUNABLES = {'preference_item': TunableReference(description='\n            The item marked by the preference of the owner.\n            ', manager=services.get_instance_manager(sims4.resources.Types.CAS_PREFERENCE_ITEM), tuning_group=GroupNames.SPECIAL_CASES)}

    @constproperty
    def is_preference_trait():
        return True

    @classproperty
    def preference_category(cls):
        return cls.preference_item.cas_preference_category

    @classproperty
    def decorator_preference(cls):
        return cls.preference_category in PreferenceTuning.DECORATOR_CAREER_PREFERENCE_CATEGORIES

    @classproperty
    def is_object_preference(cls):
        return cls.preference_item.preference_subject == PreferenceSubject.OBJECT

    @classproperty
    def is_preference_subject(cls, subject):
        return cls.preference_item.preference_subject == subject

    @classproperty
    def is_preference_subject_in_subject_set(cls, subject_set):
        return cls.preference_item.preference_subject in subject_set

    @classmethod
    def _verify_tuning_callback(cls):
        super()._verify_tuning_callback()
        if cls.decorator_preference:
            preference_item = cls.preference_item
            if hasattr(preference_item, 'object_item_def'):
                preference_item_object = preference_item.object_item_def
                if hasattr(preference_item_object, 'tag_set'):
                    tag_set = preference_item_object.tag_set
                    if not tag_set:
                        logger.error('Preference {}: For Decorator Preferences, Object Item Def must be tuned to use tags', cls)
                    test_type = preference_item_object.test_type
                    if test_type != test_type.CONTAINS_ANY_TAG_IN_SET:
                        logger.error('Preference {} is set up to use tags, but is not using test type CONTAINS_ANY_TAG_IN_SET', cls)
                else:
                    logger.error('Preference {} For Decorator Preferences, Object Item Def be tuned to use tags', cls)
