import event_testing.test_baseimport servicesfrom caches import cached_testfrom event_testing.results import TestResultfrom interactions import ParticipantTypefrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableEnumEntry, TunableVariant, TunableTuple, Tunable
class GraduationTest(HasTunableSingletonFactory, AutoFactoryInit, event_testing.test_base.BaseTest):
    GRADUATE = 0
    VALEDICTORIAN = 1
    ANY = 0
    CURRENT = 1
    WAITING = 2
    MATCH_ALL = 0
    MATCH_ANY = 1
    MATCH_NONE = 2
    FACTORY_TUNABLES = {'subject': TunableEnumEntry(description='\n            The Sim whose graduation status to check.\n            ', tunable_type=ParticipantType, default=ParticipantType.Actor), 'test': TunableVariant(description='\n            What type of test to run.\n            ', graduate=TunableTuple(description='\n                Test for whether or not the Sim is a current graduate.\n                ', locked_args={'test_type': GRADUATE}), valedictorian=TunableTuple(description='\n                Test whether or not the Sim is the valedictorian.\n                ', locked_args={'test_type': VALEDICTORIAN}), default='graduate'), 'when': TunableVariant(description='\n            Whether or not the Sim is a currently graduating, waiting to graduate, or either.\n            ', current=TunableTuple(description='\n                If selected, the Sim will need to be graduating in the current/next graduation.\n                ', locked_args={'time_type': CURRENT}), waiting=TunableTuple(description='\n                If selected, the Sim will need to be waiting for the current/next graduation to end a new graduation to \n                be scheduled before graduating.\n                ', locked_args={'time_type': WAITING}), either=TunableTuple(description="\n                If selected, it doesn't matter if the Sim is graduating in the next graduation or waiting.\n                ", locked_args={'time_type': ANY}), default='current'), 'match': TunableVariant(description='\n            When applying tests to more than one participant, this field determines if just passing any Sim in the \n            participants is enough to return True, or if you must pass every Sim in the participants for the test to \n            return True\n            ', any=TunableTuple(description='\n                If any of the tuned participants passes the test the entire test will return True.\n                ', locked_args={'match_type': MATCH_ANY}), all=TunableTuple(description='\n                Only if all of the tuned participants passes the test will the return be True.\n                ', locked_args={'match_type': MATCH_ALL}), none=TunableTuple(description='\n                Only if none of the tuned participants pass the test will this return True. If anyone does pass it will\n                return False.\n                ', locked_args={'match_type': MATCH_NONE}), default='any')}

    def get_expected_args(self):
        return {'subjects': self.subject}

    @cached_test
    def __call__(self, subjects):
        graduation_service = services.get_graduation_service()
        for subject in subjects:
            if self.test.test_type == self.GRADUATE:
                result = self._graduate_test(graduation_service, subject)
            else:
                result = self._valedictorian_test(graduation_service, subject)
            if result and self.match.match_type == self.MATCH_NONE:
                return TestResult(False, 'Graduation Test Failed: Tuned to Match None and {} matched', subject, tooltip=self.tooltip)
            if result or self.match.match_type == self.MATCH_ALL:
                return TestResult(False, "Graduation Test Failed: Tuned to Match All and {} didn't match.", subject, tooltip=self.tooltip)
            if result and self.match.match_type == self.MATCH_ANY:
                return TestResult.TRUE
        if self.match.match_type == self.MATCH_ANY:
            return TestResult(False, 'Graduation Test Failed: No subjects matched the test', tooltip=self.tooltip)
        return TestResult.TRUE

    def _graduate_test(self, graduation_service, subject):
        if self.when.time_type == self.CURRENT:
            return graduation_service.is_sim_info_graduating(subject)
        if self.when.time_type == self.WAITING:
            return graduation_service.is_sim_info_waiting_to_graduate(subject)
        return graduation_service.is_sim_info_graduating(subject) or graduation_service.is_sim_info_waiting_to_graduate(subject)

    def _valedictorian_test(self, graduation_service, subject):
        if self.when.time_type == self.CURRENT:
            return graduation_service.is_current_valedictorian(subject)
        if self.when.time_type == self.WAITING:
            return graduation_service.is_waiting_valedictorian(subject)
        return graduation_service.is_current_valedictorian(subject) or graduation_service.is_waiting_valedictorian(subject)
