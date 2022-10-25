from sims4.tuning.dynamic_enum import DynamicEnumfrom sims4.tuning.tunable import TunableMapping, TunableRange, TunableEnumEntry
class ObjectRoutingPriority(DynamicEnum):
    NONE = 0
    CRITICAL = 1

    @staticmethod
    def compare(x, y):
        if x == y:
            return 0
        if x == ObjectRoutingPriority.CRITICAL or y == ObjectRoutingPriority.NONE:
            return -1
        if x == ObjectRoutingPriority.NONE or y == ObjectRoutingPriority.CRITICAL:
            return 1
        else:
            value_map = ObjectRoutingPriorityTuning.PRIORITY_SCORE_VALUE
            return value_map[y] - value_map[x]

    @staticmethod
    def get_priority_value_string(priority):
        if priority is ObjectRoutingPriority.NONE:
            return 'Min'
        if priority is ObjectRoutingPriority.CRITICAL:
            return 'Max'
        else:
            return str(ObjectRoutingPriorityTuning.PRIORITY_SCORE_VALUE[priority])

class ObjectRoutingPriorityTuning:
    PRIORITY_SCORE_VALUE = TunableMapping(description='\n        A mapping of ObjectRoutingPriority to a numerical value.\n        ', key_type=TunableEnumEntry(tunable_type=ObjectRoutingPriority, default=ObjectRoutingPriority.NONE, invalid_enums=(ObjectRoutingPriority.NONE, ObjectRoutingPriority.CRITICAL)), value_type=TunableRange(description='\n            The value associated with this ObjectRoutingPriority. ObjectRoutingBehaviors with a higher value\n            priority will be allowed to route more often when at the routing SoftCap.\n            ', tunable_type=float, default=1, minimum=0))
