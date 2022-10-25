from google.protobuf import descriptor
class IdList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _IDLIST

class GameInstanceInfoPB(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GAMEINSTANCEINFOPB

class UserEntitlement(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _USERENTITLEMENT

class UserEntitlementMap(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _USERENTITLEMENTMAP

class AchievementItem(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ACHIEVEMENTITEM

class AchievementList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ACHIEVEMENTLIST

class AchievementMsg(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ACHIEVEMENTMSG

class UserShoppingCartItem(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _USERSHOPPINGCARTITEM

class UserShoppingCart(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _USERSHOPPINGCART

class Uint64Value(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _UINT64VALUE

class Uint64List(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _UINT64LIST

class BoolValue(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _BOOLVALUE

class HouseholdSimIds(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _HOUSEHOLDSIMIDS

class Schedule(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class ScheduleEntry(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _SCHEDULE_SCHEDULEENTRY

    DESCRIPTOR = _SCHEDULE

class SimPronoun(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SIMPRONOUN

class SimPronounList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SIMPRONOUNLIST
