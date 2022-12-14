from event_testing.resolver import DoubleSimResolverfrom event_testing.results import TestResultfrom caches import cached_testfrom interactions import ParticipantTypeSinglefrom interactions.constraint_variants import TunableGeometricConstraintVariantfrom interactions.constraints import Anywherefrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableList, TunableEnumEntry, Tunableimport assertionsimport event_testing.test_baseimport interactions.constraintsimport servicesimport sims4.logimport sims4.tuninglogger = sims4.log.Logger('ConstraintTests', default_owner='rmccord')
class SimsInConstraintTests(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    test_events = ()

    @staticmethod
    def _verify_tunable_callback(instance_class, tunable_name, source, value):
        value._validate_recursion(value.test_set, source, tunable_name)

    FACTORY_TUNABLES = {'verify_tunable_callback': _verify_tunable_callback, 'constraints': TunableList(description='\n            A list of constraints that, when intersected, will be used to find\n            all Sims we care about.\n            ', tunable=TunableGeometricConstraintVariant(description='\n                A constraint that will determine what Sims to test.\n                '), minlength=1), 'must_be_line_of_sight': Tunable(description="\n            If enabled, sims that succeed in the LOS test won't fail other tests when determining\n            the test results.\n            ", tunable_type=bool, default=False), 'constraints_target': TunableEnumEntry(description='\n            The target used to generate constraints relative to.\n            ', tunable_type=ParticipantTypeSingle, default=ParticipantTypeSingle.Object), 'test_actor': TunableEnumEntry(description='\n            The actor used to test Sims in the constraint relative to.\n            ', tunable_type=ParticipantTypeSingle, default=ParticipantTypeSingle.Object), 'test_set': sims4.tuning.tunable.TunableReference(description='\n            A test set instance that will be run on all Sims in the tuned\n            constraint. If any Sims fail the test set instance, this test will\n            fail.\n            \n            Note: A DoubleSimResolver will be used to run these tests. So the\n            Test Actor will be the Actor participant, and Target will be a Sim\n            in the constraint.\n            ', manager=services.get_instance_manager(sims4.resources.Types.SNIPPET), class_restrictions=('TestSetInstance',)), 'minimum_sim_count': sims4.tuning.tunable.OptionalTunable(description='\n            If set, will only pass the test if at least this many sims are\n            valid.\n            ', tunable=int)}

    @classmethod
    @assertions.not_recursive
    def _validate_recursion(cls, test_set_instance, source, tunable_name):
        for test_group in test_set_instance.test:
            for test in test_group:
                if isinstance(test, cls):
                    try:
                        cls._validate_recursion(test.test_set, source, tunable_name)
                    except AssertionError:
                        logger.error('{} is a test set instance in {}: {} but that creates a circular dependency', test.test_set, source, tunable_name, owner='rmccord')

    def get_expected_args(self):
        return {'constraint_targets': self.constraints_target, 'test_actors': self.test_actor}

    @cached_test
    def __call__(self, constraint_targets=(), test_actors=()):
        test_actor = test_actors[0] if test_actors else None
        sim_info_manager = services.sim_info_manager()
        instanced_sims = list(sim_info_manager.instanced_sims_gen())
        for target in constraint_targets:
            if target.is_sim:
                target = target.get_sim_instance()
                if target is None:
                    pass
                else:
                    total_constraint = Anywhere()
                    for tuned_constraint in self.constraints:
                        total_constraint = total_constraint.intersect(tuned_constraint.create_constraint(None, target))
                        if not total_constraint.valid:
                            return TestResult(False, 'Constraint {} relative to {} is invalid.', tuned_constraint, target, tooltip=self.tooltip)
                    object_constraint = interactions.constraints.Position(target._get_locations_for_posture_internal_forward_wall_padding(), routing_surface=target.routing_surface)
                    sim_count = 0
                    for sim in instanced_sims:
                        if total_constraint.geometry.test_transform(sim.transform) and (total_constraint.is_routing_surface_valid(sim.routing_surface) and total_constraint.is_location_water_depth_valid(sim.location)) and total_constraint.is_location_terrain_tags_valid(sim.location):
                            if self.test_set(DoubleSimResolver(test_actor, sim.sim_info)):
                                sim_count += 1
                            elif not (self.must_be_line_of_sight and (sim.sim_info is test_actor or object_constraint.intersect(sim.lineofsight_component.constraint).valid)):
                                sim_count += 1
                            else:
                                return TestResult(False, 'Sims In Constraint Test Failed.', tooltip=self.tooltip)
                    if self.minimum_sim_count and sim_count < self.minimum_sim_count:
                        return TestResult(False, 'Not enough sims passed the test. Passed: {0}, Minimum Needed: {1}', sim_count, self.minimum_sim_count)
            else:
                total_constraint = Anywhere()
                for tuned_constraint in self.constraints:
                    total_constraint = total_constraint.intersect(tuned_constraint.create_constraint(None, target))
                    if not total_constraint.valid:
                        return TestResult(False, 'Constraint {} relative to {} is invalid.', tuned_constraint, target, tooltip=self.tooltip)
                object_constraint = interactions.constraints.Position(target._get_locations_for_posture_internal_forward_wall_padding(), routing_surface=target.routing_surface)
                sim_count = 0
                for sim in instanced_sims:
                    if total_constraint.geometry.test_transform(sim.transform) and (total_constraint.is_routing_surface_valid(sim.routing_surface) and total_constraint.is_location_water_depth_valid(sim.location)) and total_constraint.is_location_terrain_tags_valid(sim.location):
                        if self.test_set(DoubleSimResolver(test_actor, sim.sim_info)):
                            sim_count += 1
                        elif not (self.must_be_line_of_sight and (sim.sim_info is test_actor or object_constraint.intersect(sim.lineofsight_component.constraint).valid)):
                            sim_count += 1
                        else:
                            return TestResult(False, 'Sims In Constraint Test Failed.', tooltip=self.tooltip)
                if self.minimum_sim_count and sim_count < self.minimum_sim_count:
                    return TestResult(False, 'Not enough sims passed the test. Passed: {0}, Minimum Needed: {1}', sim_count, self.minimum_sim_count)
        return TestResult.TRUE
