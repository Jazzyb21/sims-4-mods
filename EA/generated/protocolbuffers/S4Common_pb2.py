from google.protobuf import descriptorfrom google.protobuf import messagefrom google.protobuf import reflectionfrom google.protobuf import descriptor_pb2DESCRIPTOR = descriptor.FileDescriptor(name='S4Common.proto', package='EA.Sims4', serialized_pb='\n\x0eS4Common.proto\x12\x08EA.Sims4"\x19\n\x06IdList\x12\x0f\n\x03ids\x18\x01 \x03(\x06B\x02\x10\x01"~\n\x12GameInstanceInfoPB\x12\x0f\n\x07zone_id\x18\x01 \x02(\x04\x12\x10\n\x08world_id\x18\x02 \x01(\r\x12\x19\n\x11neighborhood_name\x18\x03 \x01(\t\x12\x11\n\tzone_name\x18\x04 \x01(\t\x12\x17\n\x0fzone_session_id\x18\x05 \x01(\x04"�\x03\n\x0fUserEntitlement\x12\x16\n\x0eentitlement_id\x18\x01 \x01(\x04\x12\x0f\n\x07version\x18\x02 \x01(\r\x12\x12\n\nproduct_id\x18\x03 \x01(\x04\x12\x1a\n\x12last_modified_date\x18\x04 \x01(\x04\x12\x13\n\x0bproduct_sku\x18\x05 \x01(\x04\x12\x15\n\nview_state\x18\x06 \x01(\r:\x010\x12\x1a\n\rinstall_state\x18\x07 \x01(\r:\x03100\x12\x16\n\x0eterminate_date\x18\t \x01(\x04\x12\x13\n\x0btrial_state\x18\n \x01(\r\x12\x12\n\ngrant_date\x18\x0b \x01(\x04\x12\x18\n\x10trial_view_state\x18\x0c \x01(\r",\n\x0eTrialStateMask\x12\x1a\n\x16MASK_TRIAL_ENTITLEMENT\x10\x10"z\n\nTrialState\x12\x14\n\x10TRIAL_STATE_NONE\x10\x00\x12\x19\n\x15TRIAL_STATE_CONVERTED\x10\x01\x12\x1c\n\x18TRIAL_STATE_TRIAL_ACTIVE\x10\x10\x12\x1d\n\x19TRIAL_STATE_TRIAL_EXPIRED\x10\x11"a\n\x12UserEntitlementMap\x12/\n\x0centitlements\x18\x01 \x03(\x0b2\x19.EA.Sims4.UserEntitlement\x12\x1a\n\x12last_modified_date\x18\x02 \x01(\x04"�\x01\n\x0fAchievementItem\x12\n\n\x02id\x18\x01 \x01(\r\x12\x10\n\x08progress\x18\x02 \x01(\r\x12\x13\n\x0btotalpoints\x18\x03 \x01(\r\x12\x13\n\x0brepeatcount\x18\x04 \x01(\r\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x0c\n\x04desc\x18\x06 \x01(\t\x12\r\n\x05howto\x18\x07 \x01(\t\x12\x0f\n\x07imageid\x18\x08 \x01(\t\x12\x11\n\tgrantdate\x18\t \x01(\x04\x12\x12\n\nexpiredate\x18\n \x01(\x04"b\n\x0fAchievementList\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08gamename\x18\x02 \x01(\t\x12/\n\x0cachievements\x18\x03 \x03(\x0b2\x19.EA.Sims4.AchievementItem"\\\n\x0eAchievementMsg\x12\x12\n\nresultcode\x18\x01 \x01(\x05\x12\x0c\n\x04mode\x18\x02 \x01(\r\x12(\n\x05lists\x18\x03 \x03(\x0b2\x19.EA.Sims4.AchievementList"�\x01\n\x14UserShoppingCartItem\x12\x17\n\x0fentitlement_tag\x18\x01 \x01(\t\x12\x10\n\x08offer_id\x18\x02 \x01(\t\x12\x10\n\x08quantity\x18\x03 \x01(\r\x12\x16\n\x0eoverride_price\x18\x04 \x01(\x01\x12\x12\n\nunit_price\x18\x05 \x01(\x01\x12\x18\n\x10ientitlement_tag\x18\x06 \x01(\x04\x12\x10\n\x08entry_id\x18\x07 \x01(\x04"]\n\x10UserShoppingCart\x12-\n\x05items\x18\x01 \x03(\x0b2\x1e.EA.Sims4.UserShoppingCartItem\x12\x1a\n\x12last_modified_date\x18\x02 \x01(\t"\x1c\n\x0bUint64Value\x12\r\n\x05value\x18\x01 \x02(\x04"3\n\nUint64List\x12%\n\x06values\x18\x01 \x03(\x0b2\x15.EA.Sims4.Uint64Value"\x1a\n\tBoolValue\x12\r\n\x05value\x18\x01 \x02(\x08"<\n\x0fHouseholdSimIds\x12\x14\n\x0chousehold_id\x18\x01 \x01(\x06\x12\x13\n\x07sim_ids\x18\x02 \x03(\x06B\x02\x10\x01"�\x03\n\x08Schedule\x12:\n\x10schedule_entries\x18\x01 \x03(\x0b2 .EA.Sims4.Schedule.ScheduleEntry\x1a\x83\x03\n\rScheduleEntry\x12>\n\x04days\x18\x01 \x03(\x0e2,.EA.Sims4.Schedule.ScheduleEntry.ScheduleDayB\x02\x10\x01\x12\x12\n\nstart_hour\x18\x02 \x01(\r\x12\x14\n\x0cstart_minute\x18\x03 \x01(\r\x12\x10\n\x08duration\x18\x04 \x01(\x02\x12O\n\x13schedule_shift_type\x18\x05 \x01(\x0e22.EA.Sims4.Schedule.ScheduleEntry.ScheduleShiftType"i\n\x0bScheduleDay\x12\n\n\x06SUNDAY\x10\x00\x12\n\n\x06MONDAY\x10\x01\x12\x0b\n\x07TUESDAY\x10\x02\x12\r\n\tWEDNESDAY\x10\x03\x12\x0c\n\x08THURSDAY\x10\x04\x12\n\n\x06FRIDAY\x10\x05\x12\x0c\n\x08SATURDAY\x10\x06":\n\x11ScheduleShiftType\x12\x0b\n\x07ALL_DAY\x10\x00\x12\x0b\n\x07MORNING\x10\x01\x12\x0b\n\x07EVENING\x10\x02"�\x01\n\nSimPronoun\x122\n\x04case\x18\x01 \x01(\x0e2$.EA.Sims4.SimPronoun.GrammaticalCase\x12\x0f\n\x07pronoun\x18\x02 \x01(\t"\x82\x01\n\x0fGrammaticalCase\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nSUBJECTIVE\x10\x01\x12\r\n\tOBJECTIVE\x10\x02\x12\x18\n\x14POSSESSIVE_DEPENDENT\x10\x03\x12\x1a\n\x16POSSESSIVE_INDEPENDENT\x10\x04\x12\r\n\tREFLEXIVE\x10\x05"8\n\x0eSimPronounList\x12&\n\x08pronouns\x18\x01 \x03(\x0b2\x14.EA.Sims4.SimPronoun*�\x01\n\tUserState\x12\x15\n\x11userstate_pending\x10\x01\x12\x17\n\x13userstate_logged_in\x10\x02\x12\x18\n\x14userstate_logged_out\x10\x03\x12\x1a\n\x16userstate_timedout_out\x10\x04\x12\x17\n\x13userstate_bad_login\x10\x05\x12\x1b\n\x17connected_to_mtx_server\x10d\x12!\n\x1cconnected_to_exchange_server\x10�\x01\x12\x1f\n\x1aconnected_to_social_server\x10�\x02')_USERSTATE = descriptor.EnumDescriptor(name='UserState', full_name='EA.Sims4.UserState', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='userstate_pending', index=0, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='userstate_logged_in', index=1, number=2, options=None, type=None), descriptor.EnumValueDescriptor(name='userstate_logged_out', index=2, number=3, options=None, type=None), descriptor.EnumValueDescriptor(name='userstate_timedout_out', index=3, number=4, options=None, type=None), descriptor.EnumValueDescriptor(name='userstate_bad_login', index=4, number=5, options=None, type=None), descriptor.EnumValueDescriptor(name='connected_to_mtx_server', index=5, number=100, options=None, type=None), descriptor.EnumValueDescriptor(name='connected_to_exchange_server', index=6, number=200, options=None, type=None), descriptor.EnumValueDescriptor(name='connected_to_social_server', index=7, number=300, options=None, type=None)], containing_type=None, options=None, serialized_start=2290, serialized_end=2525)userstate_pending = 1userstate_logged_in = 2userstate_logged_out = 3userstate_timedout_out = 4userstate_bad_login = 5connected_to_mtx_server = 100connected_to_exchange_server = 200connected_to_social_server = 300_USERENTITLEMENT_TRIALSTATEMASK = descriptor.EnumDescriptor(name='TrialStateMask', full_name='EA.Sims4.UserEntitlement.TrialStateMask', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='MASK_TRIAL_ENTITLEMENT', index=0, number=16, options=None, type=None)], containing_type=None, options=None, serialized_start=455, serialized_end=499)_USERENTITLEMENT_TRIALSTATE = descriptor.EnumDescriptor(name='TrialState', full_name='EA.Sims4.UserEntitlement.TrialState', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='TRIAL_STATE_NONE', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='TRIAL_STATE_CONVERTED', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='TRIAL_STATE_TRIAL_ACTIVE', index=2, number=16, options=None, type=None), descriptor.EnumValueDescriptor(name='TRIAL_STATE_TRIAL_EXPIRED', index=3, number=17, options=None, type=None)], containing_type=None, options=None, serialized_start=501, serialized_end=623)_SCHEDULE_SCHEDULEENTRY_SCHEDULEDAY = descriptor.EnumDescriptor(name='ScheduleDay', full_name='EA.Sims4.Schedule.ScheduleEntry.ScheduleDay', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='SUNDAY', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='MONDAY', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='TUESDAY', index=2, number=2, options=None, type=None), descriptor.EnumValueDescriptor(name='WEDNESDAY', index=3, number=3, options=None, type=None), descriptor.EnumValueDescriptor(name='THURSDAY', index=4, number=4, options=None, type=None), descriptor.EnumValueDescriptor(name='FRIDAY', index=5, number=5, options=None, type=None), descriptor.EnumValueDescriptor(name='SATURDAY', index=6, number=6, options=None, type=None)], containing_type=None, options=None, serialized_start=1847, serialized_end=1952)_SCHEDULE_SCHEDULEENTRY_SCHEDULESHIFTTYPE = descriptor.EnumDescriptor(name='ScheduleShiftType', full_name='EA.Sims4.Schedule.ScheduleEntry.ScheduleShiftType', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='ALL_DAY', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='MORNING', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='EVENING', index=2, number=2, options=None, type=None)], containing_type=None, options=None, serialized_start=1954, serialized_end=2012)_SIMPRONOUN_GRAMMATICALCASE = descriptor.EnumDescriptor(name='GrammaticalCase', full_name='EA.Sims4.SimPronoun.GrammaticalCase', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='UNKNOWN', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='SUBJECTIVE', index=1, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='OBJECTIVE', index=2, number=2, options=None, type=None), descriptor.EnumValueDescriptor(name='POSSESSIVE_DEPENDENT', index=3, number=3, options=None, type=None), descriptor.EnumValueDescriptor(name='POSSESSIVE_INDEPENDENT', index=4, number=4, options=None, type=None), descriptor.EnumValueDescriptor(name='REFLEXIVE', index=5, number=5, options=None, type=None)], containing_type=None, options=None, serialized_start=2099, serialized_end=2229)_IDLIST = descriptor.Descriptor(name='IdList', full_name='EA.Sims4.IdList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='ids', full_name='EA.Sims4.IdList.ids', index=0, number=1, type=6, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01'))], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=28, serialized_end=53)_GAMEINSTANCEINFOPB = descriptor.Descriptor(name='GameInstanceInfoPB', full_name='EA.Sims4.GameInstanceInfoPB', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='zone_id', full_name='EA.Sims4.GameInstanceInfoPB.zone_id', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='world_id', full_name='EA.Sims4.GameInstanceInfoPB.world_id', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='neighborhood_name', full_name='EA.Sims4.GameInstanceInfoPB.neighborhood_name', index=2, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='zone_name', full_name='EA.Sims4.GameInstanceInfoPB.zone_name', index=3, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='zone_session_id', full_name='EA.Sims4.GameInstanceInfoPB.zone_session_id', index=4, number=5, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=55, serialized_end=181)_USERENTITLEMENT = descriptor.Descriptor(name='UserEntitlement', full_name='EA.Sims4.UserEntitlement', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='entitlement_id', full_name='EA.Sims4.UserEntitlement.entitlement_id', index=0, number=1, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='version', full_name='EA.Sims4.UserEntitlement.version', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='product_id', full_name='EA.Sims4.UserEntitlement.product_id', index=2, number=3, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='last_modified_date', full_name='EA.Sims4.UserEntitlement.last_modified_date', index=3, number=4, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='product_sku', full_name='EA.Sims4.UserEntitlement.product_sku', index=4, number=5, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='view_state', full_name='EA.Sims4.UserEntitlement.view_state', index=5, number=6, type=13, cpp_type=3, label=1, has_default_value=True, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='install_state', full_name='EA.Sims4.UserEntitlement.install_state', index=6, number=7, type=13, cpp_type=3, label=1, has_default_value=True, default_value=100, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='terminate_date', full_name='EA.Sims4.UserEntitlement.terminate_date', index=7, number=9, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='trial_state', full_name='EA.Sims4.UserEntitlement.trial_state', index=8, number=10, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='grant_date', full_name='EA.Sims4.UserEntitlement.grant_date', index=9, number=11, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='trial_view_state', full_name='EA.Sims4.UserEntitlement.trial_view_state', index=10, number=12, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_USERENTITLEMENT_TRIALSTATEMASK, _USERENTITLEMENT_TRIALSTATE], options=None, is_extendable=False, extension_ranges=[], serialized_start=184, serialized_end=623)_USERENTITLEMENTMAP = descriptor.Descriptor(name='UserEntitlementMap', full_name='EA.Sims4.UserEntitlementMap', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='entitlements', full_name='EA.Sims4.UserEntitlementMap.entitlements', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='last_modified_date', full_name='EA.Sims4.UserEntitlementMap.last_modified_date', index=1, number=2, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=625, serialized_end=722)_ACHIEVEMENTITEM = descriptor.Descriptor(name='AchievementItem', full_name='EA.Sims4.AchievementItem', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='id', full_name='EA.Sims4.AchievementItem.id', index=0, number=1, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='progress', full_name='EA.Sims4.AchievementItem.progress', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='totalpoints', full_name='EA.Sims4.AchievementItem.totalpoints', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='repeatcount', full_name='EA.Sims4.AchievementItem.repeatcount', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.AchievementItem.name', index=4, number=5, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='desc', full_name='EA.Sims4.AchievementItem.desc', index=5, number=6, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='howto', full_name='EA.Sims4.AchievementItem.howto', index=6, number=7, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='imageid', full_name='EA.Sims4.AchievementItem.imageid', index=7, number=8, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='grantdate', full_name='EA.Sims4.AchievementItem.grantdate', index=8, number=9, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='expiredate', full_name='EA.Sims4.AchievementItem.expiredate', index=9, number=10, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=725, serialized_end=913)_ACHIEVEMENTLIST = descriptor.Descriptor(name='AchievementList', full_name='EA.Sims4.AchievementList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.AchievementList.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='gamename', full_name='EA.Sims4.AchievementList.gamename', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='achievements', full_name='EA.Sims4.AchievementList.achievements', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=915, serialized_end=1013)_ACHIEVEMENTMSG = descriptor.Descriptor(name='AchievementMsg', full_name='EA.Sims4.AchievementMsg', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='resultcode', full_name='EA.Sims4.AchievementMsg.resultcode', index=0, number=1, type=5, cpp_type=1, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='mode', full_name='EA.Sims4.AchievementMsg.mode', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='lists', full_name='EA.Sims4.AchievementMsg.lists', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1015, serialized_end=1107)_USERSHOPPINGCARTITEM = descriptor.Descriptor(name='UserShoppingCartItem', full_name='EA.Sims4.UserShoppingCartItem', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='entitlement_tag', full_name='EA.Sims4.UserShoppingCartItem.entitlement_tag', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='offer_id', full_name='EA.Sims4.UserShoppingCartItem.offer_id', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='quantity', full_name='EA.Sims4.UserShoppingCartItem.quantity', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='override_price', full_name='EA.Sims4.UserShoppingCartItem.override_price', index=3, number=4, type=1, cpp_type=5, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='unit_price', full_name='EA.Sims4.UserShoppingCartItem.unit_price', index=4, number=5, type=1, cpp_type=5, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='ientitlement_tag', full_name='EA.Sims4.UserShoppingCartItem.ientitlement_tag', index=5, number=6, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='entry_id', full_name='EA.Sims4.UserShoppingCartItem.entry_id', index=6, number=7, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1110, serialized_end=1281)_USERSHOPPINGCART = descriptor.Descriptor(name='UserShoppingCart', full_name='EA.Sims4.UserShoppingCart', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='items', full_name='EA.Sims4.UserShoppingCart.items', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='last_modified_date', full_name='EA.Sims4.UserShoppingCart.last_modified_date', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1283, serialized_end=1376)_UINT64VALUE = descriptor.Descriptor(name='Uint64Value', full_name='EA.Sims4.Uint64Value', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='value', full_name='EA.Sims4.Uint64Value.value', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1378, serialized_end=1406)_UINT64LIST = descriptor.Descriptor(name='Uint64List', full_name='EA.Sims4.Uint64List', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='values', full_name='EA.Sims4.Uint64List.values', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1408, serialized_end=1459)_BOOLVALUE = descriptor.Descriptor(name='BoolValue', full_name='EA.Sims4.BoolValue', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='value', full_name='EA.Sims4.BoolValue.value', index=0, number=1, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1461, serialized_end=1487)_HOUSEHOLDSIMIDS = descriptor.Descriptor(name='HouseholdSimIds', full_name='EA.Sims4.HouseholdSimIds', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='household_id', full_name='EA.Sims4.HouseholdSimIds.household_id', index=0, number=1, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='sim_ids', full_name='EA.Sims4.HouseholdSimIds.sim_ids', index=1, number=2, type=6, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01'))], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1489, serialized_end=1549)_SCHEDULE_SCHEDULEENTRY = descriptor.Descriptor(name='ScheduleEntry', full_name='EA.Sims4.Schedule.ScheduleEntry', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='days', full_name='EA.Sims4.Schedule.ScheduleEntry.days', index=0, number=1, type=14, cpp_type=8, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01')), descriptor.FieldDescriptor(name='start_hour', full_name='EA.Sims4.Schedule.ScheduleEntry.start_hour', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='start_minute', full_name='EA.Sims4.Schedule.ScheduleEntry.start_minute', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='duration', full_name='EA.Sims4.Schedule.ScheduleEntry.duration', index=3, number=4, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='schedule_shift_type', full_name='EA.Sims4.Schedule.ScheduleEntry.schedule_shift_type', index=4, number=5, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_SCHEDULE_SCHEDULEENTRY_SCHEDULEDAY, _SCHEDULE_SCHEDULEENTRY_SCHEDULESHIFTTYPE], options=None, is_extendable=False, extension_ranges=[], serialized_start=1625, serialized_end=2012)_SCHEDULE = descriptor.Descriptor(name='Schedule', full_name='EA.Sims4.Schedule', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='schedule_entries', full_name='EA.Sims4.Schedule.schedule_entries', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[_SCHEDULE_SCHEDULEENTRY], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1552, serialized_end=2012)_SIMPRONOUN = descriptor.Descriptor(name='SimPronoun', full_name='EA.Sims4.SimPronoun', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='case', full_name='EA.Sims4.SimPronoun.case', index=0, number=1, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='pronoun', full_name='EA.Sims4.SimPronoun.pronoun', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_SIMPRONOUN_GRAMMATICALCASE], options=None, is_extendable=False, extension_ranges=[], serialized_start=2015, serialized_end=2229)_SIMPRONOUNLIST = descriptor.Descriptor(name='SimPronounList', full_name='EA.Sims4.SimPronounList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='pronouns', full_name='EA.Sims4.SimPronounList.pronouns', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=2231, serialized_end=2287)_USERENTITLEMENT_TRIALSTATEMASK.containing_type = _USERENTITLEMENT_USERENTITLEMENT_TRIALSTATE.containing_type = _USERENTITLEMENT_USERENTITLEMENTMAP.fields_by_name['entitlements'].message_type = _USERENTITLEMENT_ACHIEVEMENTLIST.fields_by_name['achievements'].message_type = _ACHIEVEMENTITEM_ACHIEVEMENTMSG.fields_by_name['lists'].message_type = _ACHIEVEMENTLIST_USERSHOPPINGCART.fields_by_name['items'].message_type = _USERSHOPPINGCARTITEM_UINT64LIST.fields_by_name['values'].message_type = _UINT64VALUE_SCHEDULE_SCHEDULEENTRY.fields_by_name['days'].enum_type = _SCHEDULE_SCHEDULEENTRY_SCHEDULEDAY_SCHEDULE_SCHEDULEENTRY.fields_by_name['schedule_shift_type'].enum_type = _SCHEDULE_SCHEDULEENTRY_SCHEDULESHIFTTYPE_SCHEDULE_SCHEDULEENTRY.containing_type = _SCHEDULE_SCHEDULE_SCHEDULEENTRY_SCHEDULEDAY.containing_type = _SCHEDULE_SCHEDULEENTRY_SCHEDULE_SCHEDULEENTRY_SCHEDULESHIFTTYPE.containing_type = _SCHEDULE_SCHEDULEENTRY_SCHEDULE.fields_by_name['schedule_entries'].message_type = _SCHEDULE_SCHEDULEENTRY_SIMPRONOUN.fields_by_name['case'].enum_type = _SIMPRONOUN_GRAMMATICALCASE_SIMPRONOUN_GRAMMATICALCASE.containing_type = _SIMPRONOUN_SIMPRONOUNLIST.fields_by_name['pronouns'].message_type = _SIMPRONOUNDESCRIPTOR.message_types_by_name['IdList'] = _IDLISTDESCRIPTOR.message_types_by_name['GameInstanceInfoPB'] = _GAMEINSTANCEINFOPBDESCRIPTOR.message_types_by_name['UserEntitlement'] = _USERENTITLEMENTDESCRIPTOR.message_types_by_name['UserEntitlementMap'] = _USERENTITLEMENTMAPDESCRIPTOR.message_types_by_name['AchievementItem'] = _ACHIEVEMENTITEMDESCRIPTOR.message_types_by_name['AchievementList'] = _ACHIEVEMENTLISTDESCRIPTOR.message_types_by_name['AchievementMsg'] = _ACHIEVEMENTMSGDESCRIPTOR.message_types_by_name['UserShoppingCartItem'] = _USERSHOPPINGCARTITEMDESCRIPTOR.message_types_by_name['UserShoppingCart'] = _USERSHOPPINGCARTDESCRIPTOR.message_types_by_name['Uint64Value'] = _UINT64VALUEDESCRIPTOR.message_types_by_name['Uint64List'] = _UINT64LISTDESCRIPTOR.message_types_by_name['BoolValue'] = _BOOLVALUEDESCRIPTOR.message_types_by_name['HouseholdSimIds'] = _HOUSEHOLDSIMIDSDESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULEDESCRIPTOR.message_types_by_name['SimPronoun'] = _SIMPRONOUNDESCRIPTOR.message_types_by_name['SimPronounList'] = _SIMPRONOUNLIST
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
