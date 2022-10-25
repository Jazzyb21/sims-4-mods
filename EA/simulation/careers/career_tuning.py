from protocolbuffers.DistributorOps_pb2 import Operation
class ActiveCareerType(enum.Int):
    NON_ACTIVE = 0
    ACTIVE = 1
    MULTI_SIM_ACTIVE = 2

def _get_career_notification_tunable_factory(**kwargs):
    return UiDialogNotification.TunableFactory(locked_args={'text_tokens': DEFAULT, 'icon': None, 'primary_icon_response': UiDialogResponse(text=None, ui_request=UiDialogResponse.UiDialogUiRequest.SHOW_CAREER_PANEL), 'secondary_icon': None}, **kwargs)

class CareerToneTuning(AutoFactoryInit, HasTunableSingletonFactory):
    FACTORY_TUNABLES = {'default_action_list': TunableList(description='\n            List of test to default action. Should any test pass, that will\n            be set as the default action.\n            ', tunable=TunableTuple(default_action_test=OptionalTunable(description='\n                    If enabled, test will be run on the sim. \n                    Otherwise, no test will be run and default_action tuned will\n                    automatically be chosen. There should only be one item, \n                    which is also the default item in the list which has this \n                    disabled.\n                    ', tunable=TunableTestSet(description='\n                        Test to run to figure out what the default away action \n                        should be.\n                        ')), default_action=AwayAction.TunableReference(description='\n                    Default away action tone.\n                    '))), 'optional_actions': TunableSet(description='\n            Additional selectable away action tones.\n            ', tunable=AwayAction.TunableReference(pack_safe=True)), 'leave_work_early': TunableReference(description='\n            Sim Info interaction to end work early.\n            ', manager=services.get_instance_manager(sims4.resources.Types.INTERACTION), class_restrictions='CareerLeaveWorkEarlyInteraction'), 'stay_late': OptionalTunable(description='\n            If enabled, a Sim Info interaction to extend the work session.\n            ', tunable=TunableReference(manager=services.get_instance_manager(sims4.resources.Types.INTERACTION), class_restrictions='CareerStayLateInteraction'))}

    def get_default_action(self, sim_info):
        resolver = SingleSimResolver(sim_info)
        for default_action_info in self.default_action_list:
            default_test = default_action_info.default_action_test
            if not default_test is None:
                if default_test.run_tests(resolver):
                    return default_action_info.default_action
            return default_action_info.default_action
        logger.error('Failed to find default action for career tone tuning.                       Did you forget to add a default action with no test at                       the end of the list?')
