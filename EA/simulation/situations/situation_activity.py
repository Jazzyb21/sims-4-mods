from holidays.holiday_tradition import HolidayTradition, TraditionTypefrom sims4.tuning.instances import lock_instance_tunables
class SituationActivity(HolidayTradition):
    REMOVE_INSTANCE_TUNABLES = ('pre_holiday_buffs', 'pre_holiday_buff_reason', 'holiday_buffs', 'holiday_buff_reason', 'drama_nodes_to_score', 'drama_nodes_to_run', 'additional_walkbys', 'preference', 'preference_reward_buff', 'lifecycle_actions', 'events', 'core_object_tags', 'deco_object_tags', 'business_cost_multiplier')
