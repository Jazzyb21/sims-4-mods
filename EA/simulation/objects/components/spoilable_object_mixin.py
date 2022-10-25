import operatorfrom crafting.crafting_process import loggerfrom crafting.crafting_tunable import CraftingTuningfrom objects.components import componentmethod_with_fallbackfrom objects.hovertip import TooltipFieldsCompletefrom retail.retail_component import RetailComponentimport sims4.math
class SpoilableObjectMixin:

    def __init__(self, owner, **kwargs):
        super().__init__(owner, **kwargs)
        self._spoil_listener_handle = None
        self._last_spoiled_time = None
        self._spoil_timer_state_value = CraftingTuning.SPOILED_STATE_VALUE

    def spoilable_on_add(self):
        if self.owner.state_component is not None:
            freshness_state = CraftingTuning.LOCK_FRESHNESS_STATE_VALUE.state
            if self.owner.has_state(freshness_state):
                freshness_locked_state_value = self.owner.get_state(freshness_state)
                if freshness_locked_state_value is CraftingTuning.LOCK_FRESHNESS_STATE_VALUE:
                    self._on_object_state_change(self.owner, freshness_locked_state_value.state, freshness_locked_state_value, freshness_locked_state_value)

    def spoilable_on_remove(self):
        if self._spoil_listener_handle is not None:
            spoil_tracker = self.owner.get_tracker(self._spoil_timer_state_value.state.linked_stat)
            spoil_tracker.remove_listener(self._spoil_listener_handle)

    def spoilable_on_add_hovertip(self, spoil_time_commodity_override, time_until_spoiled_string_override):
        self._add_spoil_listener(state_override=spoil_time_commodity_override)
        if time_until_spoiled_string_override is not None:
            self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time_text, time_until_spoiled_string_override)

    def spoilable_on_remove_hovertip(self):
        self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0)

    def spoilable_on_object_state_change(self, owner, state, old_value, new_value, quality_state):
        state_value = None
        if state is quality_state:
            state_value = new_value
        elif state is CraftingTuning.FRESHNESS_STATE:
            if new_value in CraftingTuning.QUALITY_STATE_VALUE_MAP:
                state_value = new_value
            else:
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, None)
                if self.owner.has_state(quality_state):
                    state_value = self.owner.get_state(quality_state)
        if state_value is not None:
            value_quality = CraftingTuning.QUALITY_STATE_VALUE_MAP.get(state_value)
            if value_quality is not None:
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality, value_quality.state_star_number)
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, None)
            else:
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality, 0)
                self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, state_value.display_name)

    def spoilable_pre_save(self):
        self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0, should_update=True)

    @staticmethod
    def object_is_spoiled(object):
        return object.has_state(CraftingTuning.SPOILED_STATE_VALUE.state) and object.get_state(CraftingTuning.SPOILED_STATE_VALUE.state) is CraftingTuning.SPOILED_STATE_VALUE

    @componentmethod_with_fallback(lambda : None)
    def post_tooltip_save_data_stored(self):
        if self._last_spoiled_time is not None:
            self._on_spoil_time_changed(None, self._last_spoiled_time)

    def _on_spoil_time_changed(self, _, spoiled_time):
        if self._last_spoiled_time is None or self._last_spoiled_time != spoiled_time:
            self._last_spoiled_time = spoiled_time
        if RetailComponent.SOLD_STATE is not None and self.owner.has_state(RetailComponent.SOLD_STATE.state) and self.owner.get_state(RetailComponent.SOLD_STATE.state) is RetailComponent.SOLD_STATE:
            self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0, should_update=True)
            return
        if spoiled_time is not None:
            time_in_ticks = spoiled_time.absolute_ticks()
            self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, time_in_ticks, should_update=True)
            logger.debug('{} will get spoiled at {}', self.owner, spoiled_time)
        else:
            self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0, should_update=True)

    def _on_spoiled(self, _):
        self._last_spoiled_time = None

    def _add_spoil_listener(self, state_override=None):
        check_operator = operator.lt
        if state_override is not None:
            self._spoil_timer_state_value = state_override.state_to_track
            check_operator = state_override.commodity_check_operator
        if self.owner.has_state(self._spoil_timer_state_value.state):
            linked_stat = self._spoil_timer_state_value.state.linked_stat
            tracker = self.owner.get_tracker(linked_stat)
            if tracker is None:
                return
            threshold = sims4.math.Threshold()
            threshold.value = self._spoil_timer_state_value.range.upper_bound
            threshold.comparison = check_operator
            self._spoil_listener_handle = tracker.create_and_add_listener(linked_stat, threshold, self._on_spoiled, on_callback_alarm_reset=self._on_spoil_time_changed)
