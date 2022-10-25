import servicesfrom singletons import DEFAULTfrom ui.ui_dialog_notification import UiDialogNotification
class UIDialogNotificationStoryProgressionDiscovery(UiDialogNotification):

    def build_msg(self, additional_tokens=(), icon_override=DEFAULT, event_id=None, career_args=None, **kwargs):
        additional_tokens = list(additional_tokens)
        (text_override, tokens) = services.get_story_progression_service().get_discovery_string()
        additional_tokens = additional_tokens + tokens
        msg = super().build_msg(additional_tokens=tuple(additional_tokens), icon_override=icon_override, event_id=event_id, career_args=career_args, text_override=text_override, **kwargs)
        return msg
