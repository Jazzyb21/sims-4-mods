import enumimport event_testing.test_baseimport servicesfrom event_testing.results import TestResultfrom interactions import ParticipantType, ParticipantTypeSingle, ParticipantTypeActorTargetSimfrom objects.components.types import ANIMAL_OBJECT_COMPONENT, ANIMAL_HOME_COMPONENTfrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, Tunable, TunableVariant, TunableEnumEntry, TunableTuplefrom tag import TunableTag
class AssignedToTargetHomeTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description="\n            Animal we're testing the assignment of.\n            ", tunable_type=ParticipantType, default=ParticipantType.Actor), 'target': TunableEnumEntry(description='\n            Target home to test that the animal is assigned to.\n            ', tunable_type=ParticipantTypeSingle, default=ParticipantType.Object)}

    def _get_expected_args(self):
        return {'test_subjects': self.subject, 'test_target': self.target}

    def _evaluate(self, negate, tooltip=None, test_subjects=(), test_target=()):
        animal_service = services.animal_service()
        if animal_service is None:
            return TestResult(False, 'Animal Service does not exist.', tooltip=tooltip)
        if not test_target:
            return TestResult(False, 'No target objects to test assignment for.', tooltip=tooltip)
        target = next(iter(test_target))
        for subject in test_subjects:
            if not subject.has_component(ANIMAL_OBJECT_COMPONENT):
                return TestResult(False, 'Subject {} does not have an Animal Object Component.', subject, tooltip=tooltip)
            if not target.has_component(ANIMAL_HOME_COMPONENT):
                return TestResult(False, 'Target {} does not have an Animal Home Component.', target, tooltip=tooltip)
            assigned_home_id = animal_service.get_animal_home_id(subject.id)
            if assigned_home_id is not None and assigned_home_id == target.id and negate:
                return TestResult(False, 'Animal {} is assigned to home {}', subject, target, tooltip=tooltip)
            if not assigned_home_id is None:
                pass
            if not negate:
                return TestResult(False, 'Animal {} is not assigned to home {}', subject, target, tooltip=tooltip)
        return TestResult.TRUE

class HomeMaxCapacityTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            Animal or home to run the test on.\n            ', tunable_type=ParticipantTypeSingle, default=ParticipantType.Actor)}

    def _get_expected_args(self):
        return {'test_subject': self.subject}

    def _evaluate(self, negate, tooltip=None, test_subject=()):
        animal_service = services.animal_service()
        if animal_service is None:
            return TestResult(False, 'Animal Service does not exist.', tooltip=tooltip)
        if not test_subject:
            return TestResult(False, 'No subject to test capacity on.', tooltip=tooltip)
        subject = next(iter(test_subject))
        animal_comp = subject.get_component(ANIMAL_OBJECT_COMPONENT)
        home_comp = subject.get_component(ANIMAL_HOME_COMPONENT)
        if animal_comp is not None:
            home_id = animal_service.get_animal_home_id(subject.id)
            if home_id is None:
                return TestResult(False, 'Animal {} is not assigned to a home.', subject, tooltip=tooltip)
            max_capacity = animal_service.get_animal_home_max_capacity(subject.id)
            current_occupancy = animal_service.get_current_occupancy(home_id)
        elif home_comp is not None:
            max_capacity = home_comp.get_max_capacity()
            current_occupancy = animal_service.get_current_occupancy(subject.id)
        elif animal_comp is None and home_comp is None:
            return TestResult(False, 'Subject {} is neither an animal nor an animal home.', subject, tooltip=tooltip)
        if current_occupancy is None:
            return TestResult(False, 'Home does not have a valid occupancy.', subject, tooltip=tooltip)
        if current_occupancy == max_capacity and negate:
            return TestResult(False, 'Home {} is at max capacity of {}', subject, max_capacity, tooltip=tooltip)
        if current_occupancy != max_capacity and not negate:
            return TestResult(False, 'Home {} is not at max capacity of {}', subject, max_capacity, tooltip=tooltip)
        return TestResult.TRUE

class HomelessTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            Animal to run the test on.\n            ', tunable_type=ParticipantType, default=ParticipantType.Actor)}

    def _get_expected_args(self):
        return {'test_subjects': self.subject}

    def _evaluate(self, negate, tooltip=None, test_subjects=()):
        animal_service = services.animal_service()
        if animal_service is None:
            return TestResult(False, 'Animal Service does not exist.', tooltip=tooltip)
        for subject in test_subjects:
            if not subject.has_component(ANIMAL_OBJECT_COMPONENT):
                return TestResult(False, 'Subject {} does not have an Animal Object Component.', subject, tooltip=tooltip)
            home_id = animal_service.get_animal_home_id(subject.id)
            if home_id is not None and not negate:
                return TestResult(False, 'Animal {} has an assigned home {}.', subject, home_id, tooltip=tooltip)
            if home_id is None and negate:
                return TestResult(False, 'Animal {} does not have an assigned home.', subject, tooltip=tooltip)
        return TestResult.TRUE

class PreferenceTypes(enum.Int):
    DISLIKE = 0
    LIKE = 1
    FAVORITE = 2

class AnimalPreferenceTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'target': TunableEnumEntry(description="\n            The animal we're targeting\n            ", tunable_type=ParticipantTypeSingle, default=ParticipantType.Object), 'tag_to_test': TunableTag(description='\n            The tag (category) to test against\n            ', filter_prefixes=('Func',)), 'preference_type': TunableEnumEntry(description="\n            The type of preference that we'll test the tag against\n            ", tunable_type=PreferenceTypes, default=PreferenceTypes.DISLIKE)}

    def _get_expected_args(self):
        return {'target': self.target}

    def _evaluate(self, negate, tooltip=None, target=()):
        target = next(iter(target))
        if target is None:
            return TestResult(False, 'Target animal is None, fix in tuning', tooltip=tooltip)
        if target.is_sim:
            target = target.get_sim_instance()
            if target is None:
                return TestResult(False, "Subject {} was a sim but couldn't get instance", target, tooltip=tooltip)
        preference_component = target.animalpreference_component
        if preference_component is None:
            return TestResult(False, "Target {} didn't have an AnimalPreferenceComponent", target, tooltip=tooltip)
        result = preference_component.test_preference_match(self.tag_to_test, self.preference_type)
        result = result if not negate else not result
        if not result:
            return TestResult(False, 'Animal did not match preference {} {}', self.tag_to_test, self.preference_type, tooltip=tooltip)
        return TestResult.TRUE

class AnimalPreferenceKnowledgeTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            The subject initiating the test\n            ', tunable_type=ParticipantTypeActorTargetSim, default=ParticipantTypeActorTargetSim.Actor), 'target': TunableEnumEntry(description="\n            The animal we're targeting\n            ", tunable_type=ParticipantTypeSingle, default=ParticipantType.Object), 'tag_to_test': TunableTag(description='\n            The tag (category) to test against\n            ', filter_prefixes=('func',))}

    def _get_expected_args(self):
        return {'subject': self.subject, 'target': self.target}

    def _evaluate(self, negate, tooltip=None, subject=(), target=()):
        subject = next(iter(subject))
        target = next(iter(target))
        if target is None or subject is None:
            return TestResult(False, 'The subject / target is None, fix in tuning', tooltip=tooltip)
        if target.is_sim:
            target = target.get_sim_instance()
            if target is None:
                return TestResult(False, "Subject {} was a sim but couldn't get instance", target, tooltip=tooltip)
        preference_component = target.animalpreference_component
        if preference_component is None:
            return TestResult(False, "Target {} didn't have an AnimalPreferenceComponent", target, tooltip=tooltip)
        household_id = subject.sim_info.household_id
        result = preference_component.test_is_preference_known(household_id, self.tag_to_test)
        result = result if not negate else not result
        if not result:
            return TestResult(False, 'Sim {} did not have knowledge of {}', subject, self.tag_to_test, tooltip=tooltip)
        return TestResult.TRUE

class AnimalGiftingCooldownTypes(enum.Int):
    GENERAL = 0
    CATEGORY = 1

class AnimalGiftingCooldownTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            The subject initiating the test\n            ', tunable_type=ParticipantTypeActorTargetSim, default=ParticipantTypeActorTargetSim.Actor), 'target': TunableEnumEntry(description="\n            The animal we're targeting\n            ", tunable_type=ParticipantTypeSingle, default=ParticipantType.Object), 'cooldown_op_variant': TunableVariant(description='\n            Whether or not this should test against the general readiness, or category readiness\n            ', general_cooldown_op=TunableTuple(description='\n                This operation tests against general readiness\n                ', locked_args={'cooldown_op': AnimalGiftingCooldownTypes.GENERAL}), category_cooldown_op=TunableTuple(description='\n                This operation tests against category readiness\n                ', tag=TunableTag(description='\n                    Which tag category to test\n                    ', filter_prefixes=('Func',)), locked_args={'cooldown_op': AnimalGiftingCooldownTypes.CATEGORY}), default='category_cooldown_op')}

    def _get_expected_args(self):
        return {'subject': self.subject, 'target': self.target}

    def _evaluate(self, negate, tooltip=None, subject=(), target=()):
        subject = next(iter(subject))
        target = next(iter(target))
        if target is None or subject is None:
            return TestResult(False, 'The subject / target is None, fix in tuning', tooltip=tooltip)
        if target.is_sim:
            target = target.get_sim_instance()
            if target is None:
                return TestResult(False, "Subject {} was a sim but couldn't get instance", target, tooltip=tooltip)
        preference_component = target.animalpreference_component
        if preference_component is None:
            return TestResult(False, "Target {} didn't have an AnimalPreferenceComponent", target, tooltip=tooltip)
        household_id = subject.sim_info.household_id
        if self.cooldown_op_variant.cooldown_op == AnimalGiftingCooldownTypes.GENERAL:
            result = preference_component.test_is_general_ready(household_id)
            result = result if not negate else not result
            if not result:
                return TestResult(False, 'General gifting was not ready for {}', target, tooltip=tooltip)
        elif self.cooldown_op_variant.cooldown_op == AnimalGiftingCooldownTypes.CATEGORY:
            tag = self.cooldown_op_variant.tag
            result = preference_component.test_is_category_ready(household_id, tag)
            result = result if not negate else not result
            if not result:
                return TestResult(False, 'Gift category {} for {} was not ready', tag, target, tooltip=tooltip)
        else:
            TestResult(False, 'No cooldown type specified, fix in tuning for {}', target, tooltip=tooltip)
        return TestResult.TRUE

class AllAnimalPreferencesKnownTest(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            The subject initiating the test\n            ', tunable_type=ParticipantTypeActorTargetSim, default=ParticipantTypeActorTargetSim.Actor), 'target': TunableEnumEntry(description="\n            The animal we're targeting\n            ", tunable_type=ParticipantTypeSingle, default=ParticipantType.Object)}

    def _get_expected_args(self):
        return {'subject': self.subject, 'target': self.target}

    def _evaluate(self, negate, tooltip=None, subject=(), target=()):
        subject = next(iter(subject))
        target = next(iter(target))
        if target is None or subject is None:
            return TestResult(False, 'The subject / target is None, fix in tuning', tooltip=tooltip)
        if target.is_sim:
            target = target.get_sim_instance()
            if target is None:
                return TestResult(False, "Subject {} was a sim but couldn't get instance", target, tooltip=tooltip)
        preference_component = target.animalpreference_component
        if preference_component is None:
            return TestResult(False, "Target {} didn't have an AnimalPreferenceComponent", target, tooltip=tooltip)
        household_id = subject.sim_info.household_id
        result = preference_component.test_are_all_preferences_known(household_id)
        result = result if not negate else not result
        if not result:
            return TestResult(False, 'All preferences were not known by {} for {}', subject, target, tooltip=tooltip)
        return TestResult.TRUE

class AnimalTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    FACTORY_TUNABLES = {'test_type': TunableVariant(description='\n            The type of animal test to run.\n            ', animal_assigned_to_target_home=AssignedToTargetHomeTest.TunableFactory(), animal_is_homeless=HomelessTest.TunableFactory(), home_is_at_max_capacity=HomeMaxCapacityTest.TunableFactory(), animal_gifting_is_ready=AnimalGiftingCooldownTest.TunableFactory(), animal_has_matching_preference=AnimalPreferenceTest.TunableFactory(), sim_has_animal_preference_knowledge=AnimalPreferenceKnowledgeTest.TunableFactory(), are_all_preferences_known=AllAnimalPreferencesKnownTest.TunableFactory()), 'negate': Tunable(description='\n            Returns the opposite of the test results.\n            ', tunable_type=bool, default=False)}

    def get_expected_args(self):
        return self.test_type._get_expected_args()

    def __call__(self, *args, **kwargs):
        return self.test_type._evaluate(self.negate, *args, tooltip=self.tooltip, **kwargs)
