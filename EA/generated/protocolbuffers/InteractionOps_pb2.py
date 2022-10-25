from google.protobuf import descriptorfrom google.protobuf import messagefrom google.protobuf import reflectionfrom google.protobuf import descriptor_pb2import protocolbuffers.ResourceKey_pb2 as ResourceKey_pb2import protocolbuffers.Localization_pb2 as Localization_pb2import protocolbuffers.UI_pb2 as UI_pb2DESCRIPTOR = descriptor.FileDescriptor(name='InteractionOps.proto', package='EA.Sims4.Network', serialized_pb='\n\x14InteractionOps.proto\x12\x10EA.Sims4.Network\x1a\x11ResourceKey.proto\x1a\x12Localization.proto\x1a\x08UI.proto"\x8d\x01\n\x0cInteractable\x12\x17\n\x0fis_interactable\x18\x01 \x02(\x08\x12\x11\n\tobject_id\x18\x02 \x02(\x06\x12\x1d\n\x12interactable_flags\x18\x03 \x01(\x04:\x010"2\n\x11InteractableFlags\x12\x10\n\x0cINTERACTABLE\x10\x01\x12\x0b\n\x07FORSALE\x10\x02"\x92\x05\n\x0bPieMenuItem\x12\n\n\x02id\x18\x01 \x02(\r\x125\n\nloc_string\x18\x02 \x02(\x0b2!.EA.Sims4.Network.LocalizedString\x12\x1a\n\x0erelated_skills\x18\x03 \x03(\x04B\x02\x10\x01\x12\x16\n\ntarget_ids\x18\x04 \x03(\x04B\x02\x10\x01\x12+\n\x04icon\x18\x05 \x01(\x0b2\x1d.EA.Sims4.Network.ResourceKey\x128\n\rdisabled_text\x18\x06 \x01(\x0b2!.EA.Sims4.Network.LocalizedString\x121\n\nscore_icon\x18\x07 \x01(\x0b2\x1d.EA.Sims4.Network.ResourceKey\x12\x14\n\x0ccategory_key\x18\t \x01(\x04\x12\x10\n\x08is_super\x18\n \x01(\x08\x12\r\n\x05score\x18\x0b \x01(\x02\x12,\n\x05icons\x18\x0c \x03(\x0b2\x1d.EA.Sims4.Network.ResourceKey\x12\x0c\n\x04mood\x18\r \x01(\x06\x12\x16\n\x0emood_intensity\x18\x0e \x01(\r\x12\x19\n\x11pie_menu_priority\x18\x0f \x01(\r\x12:\n\x0fsuccess_tooltip\x18\x10 \x01(\x0b2!.EA.Sims4.Network.LocalizedString\x12.\n\nicon_infos\x18\x11 \x03(\x0b2\x1a.EA.Sims4.Network.IconInfo\x12\x1c\n\x14display_notification\x18\x12 \x01(\x08\x12\x15\n\raffordance_id\x18\x13 \x01(\x04\x12+\n#phone_notification_control_override\x18\x14 \x01(\x08"�\x02\n\rPieMenuCreate\x12\x0b\n\x03sim\x18\x01 \x02(\x04\x12,\n\x05items\x18\x02 \x03(\x0b2\x1d.EA.Sims4.Network.PieMenuItem\x12\x1b\n\x13client_reference_id\x18\x03 \x01(\r\x12\x1b\n\x13server_reference_id\x18\x04 \x01(\r\x12?\n\x0fcategory_tokens\x18\x05 \x03(\x0b2&.EA.Sims4.Network.LocalizedStringToken\x12;\n\x10disabled_tooltip\x18\x06 \x01(\x0b2!.EA.Sims4.Network.LocalizedString\x12!\n\x19supress_social_front_page\x18\x07 \x01(\x08"\x89\x01\n\x10TravelMenuCreate\x12\x0e\n\x06sim_id\x18\x01 \x02(\x04\x12\x17\n\x0fselected_lot_id\x18\x02 \x01(\x04\x12\x19\n\x11selected_world_id\x18\x03 \x01(\r\x12\x19\n\x11selected_lot_name\x18\x04 \x01(\t\x12\x16\n\x0efriend_account\x18\x05 \x01(\t"%\n\x0eTravelMenuInfo\x12\x13\n\x07sim_ids\x18\x01 \x03(\x04B\x02\x10\x01"&\n\x12TravelMenuResponse\x12\x10\n\x08reserved\x18\x01 \x02(\x08" \n\x0eTravelInitiate\x12\x0e\n\x06zoneId\x18\x01 \x02(\x04"N\n\x11MoveInMoveOutInfo\x12\x18\n\x10moving_family_id\x18\x01 \x01(\x04\x12\x1f\n\x10is_in_game_evict\x18\x02 \x01(\x08:\x05false"\'\n\rSellRetailLot\x12\x16\n\x0eretail_zone_id\x18\x01 \x02(\x04"O\n\x10TravelSimsToZone\x12\x0f\n\x07zone_id\x18\x01 \x01(\x06\x12\x13\n\x07sim_ids\x18\x02 \x03(\x06B\x02\x10\x01\x12\x15\n\ractive_sim_id\x18\x03 \x01(\x06"H\n\x15CASAvailableZonesInfo\x12/\n\x05zones\x18\x01 \x03(\x0b2 .EA.Sims4.Network.WorldZonesInfo"\x92\x01\n\x0eWorldZonesInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x126\n\x0bdefaultName\x18\x02 \x01(\x0b2!.EA.Sims4.Network.LocalizedString\x12)\n\x05zones\x18\x03 \x03(\x0b2\x1a.EA.Sims4.Network.ZoneInfo\x12\x0f\n\x07worldId\x18\x04 \x01(\r"\x8a\x01\n\x08ZoneInfo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x03 \x01(\t\x126\n\x0bdefaultName\x18\x04 \x01(\x0b2!.EA.Sims4.Network.LocalizedString\x12\x10\n\x08world_id\x18\x05 \x01(\r\x12\x1a\n\x12lot_description_id\x18\x07 \x01(\x06"\x9a\x01\n\x19InteractionProgressUpdate\x12\x0e\n\x06sim_id\x18\x01 \x01(\x06\x12/\n\x04name\x18\x02 \x01(\x0b2!.EA.Sims4.Network.LocalizedString\x12\x0f\n\x07percent\x18\x03 \x01(\x02\x12\x13\n\x0brate_change\x18\x04 \x01(\x02\x12\x16\n\x0einteraction_id\x18\x05 \x01(\x04"e\n\x12SimTransferRequest\x12\x1b\n\x13source_household_id\x18\x01 \x01(\x06\x12\x1b\n\x13target_household_id\x18\x02 \x01(\x06\x12\x15\n\ractive_sim_id\x18\x03 \x01(\x06"F\n\x17PhoneNotificationUpdate\x12\x1b\n\x0finteraction_ids\x18\x01 \x03(\x04B\x02\x10\x01\x12\x0e\n\x06sim_id\x18\x02 \x02(\x04')_INTERACTABLE_INTERACTABLEFLAGS = descriptor.EnumDescriptor(name='InteractableFlags', full_name='EA.Sims4.Network.Interactable.InteractableFlags', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='INTERACTABLE', index=0, number=1, options=None, type=None), descriptor.EnumValueDescriptor(name='FORSALE', index=1, number=2, options=None, type=None)], containing_type=None, options=None, serialized_start=183, serialized_end=233)_INTERACTABLE = descriptor.Descriptor(name='Interactable', full_name='EA.Sims4.Network.Interactable', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='is_interactable', full_name='EA.Sims4.Network.Interactable.is_interactable', index=0, number=1, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='object_id', full_name='EA.Sims4.Network.Interactable.object_id', index=1, number=2, type=6, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='interactable_flags', full_name='EA.Sims4.Network.Interactable.interactable_flags', index=2, number=3, type=4, cpp_type=4, label=1, has_default_value=True, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_INTERACTABLE_INTERACTABLEFLAGS], options=None, is_extendable=False, extension_ranges=[], serialized_start=92, serialized_end=233)_PIEMENUITEM = descriptor.Descriptor(name='PieMenuItem', full_name='EA.Sims4.Network.PieMenuItem', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='id', full_name='EA.Sims4.Network.PieMenuItem.id', index=0, number=1, type=13, cpp_type=3, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='loc_string', full_name='EA.Sims4.Network.PieMenuItem.loc_string', index=1, number=2, type=11, cpp_type=10, label=2, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='related_skills', full_name='EA.Sims4.Network.PieMenuItem.related_skills', index=2, number=3, type=4, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01')), descriptor.FieldDescriptor(name='target_ids', full_name='EA.Sims4.Network.PieMenuItem.target_ids', index=3, number=4, type=4, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01')), descriptor.FieldDescriptor(name='icon', full_name='EA.Sims4.Network.PieMenuItem.icon', index=4, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='disabled_text', full_name='EA.Sims4.Network.PieMenuItem.disabled_text', index=5, number=6, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='score_icon', full_name='EA.Sims4.Network.PieMenuItem.score_icon', index=6, number=7, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='category_key', full_name='EA.Sims4.Network.PieMenuItem.category_key', index=7, number=9, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='is_super', full_name='EA.Sims4.Network.PieMenuItem.is_super', index=8, number=10, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='score', full_name='EA.Sims4.Network.PieMenuItem.score', index=9, number=11, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='icons', full_name='EA.Sims4.Network.PieMenuItem.icons', index=10, number=12, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='mood', full_name='EA.Sims4.Network.PieMenuItem.mood', index=11, number=13, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='mood_intensity', full_name='EA.Sims4.Network.PieMenuItem.mood_intensity', index=12, number=14, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='pie_menu_priority', full_name='EA.Sims4.Network.PieMenuItem.pie_menu_priority', index=13, number=15, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='success_tooltip', full_name='EA.Sims4.Network.PieMenuItem.success_tooltip', index=14, number=16, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='icon_infos', full_name='EA.Sims4.Network.PieMenuItem.icon_infos', index=15, number=17, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='display_notification', full_name='EA.Sims4.Network.PieMenuItem.display_notification', index=16, number=18, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='affordance_id', full_name='EA.Sims4.Network.PieMenuItem.affordance_id', index=17, number=19, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='phone_notification_control_override', full_name='EA.Sims4.Network.PieMenuItem.phone_notification_control_override', index=18, number=20, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=236, serialized_end=894)_PIEMENUCREATE = descriptor.Descriptor(name='PieMenuCreate', full_name='EA.Sims4.Network.PieMenuCreate', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='sim', full_name='EA.Sims4.Network.PieMenuCreate.sim', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='items', full_name='EA.Sims4.Network.PieMenuCreate.items', index=1, number=2, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='client_reference_id', full_name='EA.Sims4.Network.PieMenuCreate.client_reference_id', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='server_reference_id', full_name='EA.Sims4.Network.PieMenuCreate.server_reference_id', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='category_tokens', full_name='EA.Sims4.Network.PieMenuCreate.category_tokens', index=4, number=5, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='disabled_tooltip', full_name='EA.Sims4.Network.PieMenuCreate.disabled_tooltip', index=5, number=6, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='supress_social_front_page', full_name='EA.Sims4.Network.PieMenuCreate.supress_social_front_page', index=6, number=7, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=897, serialized_end=1190)_TRAVELMENUCREATE = descriptor.Descriptor(name='TravelMenuCreate', full_name='EA.Sims4.Network.TravelMenuCreate', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='sim_id', full_name='EA.Sims4.Network.TravelMenuCreate.sim_id', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='selected_lot_id', full_name='EA.Sims4.Network.TravelMenuCreate.selected_lot_id', index=1, number=2, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='selected_world_id', full_name='EA.Sims4.Network.TravelMenuCreate.selected_world_id', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='selected_lot_name', full_name='EA.Sims4.Network.TravelMenuCreate.selected_lot_name', index=3, number=4, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='friend_account', full_name='EA.Sims4.Network.TravelMenuCreate.friend_account', index=4, number=5, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1193, serialized_end=1330)_TRAVELMENUINFO = descriptor.Descriptor(name='TravelMenuInfo', full_name='EA.Sims4.Network.TravelMenuInfo', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='sim_ids', full_name='EA.Sims4.Network.TravelMenuInfo.sim_ids', index=0, number=1, type=4, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01'))], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1332, serialized_end=1369)_TRAVELMENURESPONSE = descriptor.Descriptor(name='TravelMenuResponse', full_name='EA.Sims4.Network.TravelMenuResponse', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='reserved', full_name='EA.Sims4.Network.TravelMenuResponse.reserved', index=0, number=1, type=8, cpp_type=7, label=2, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1371, serialized_end=1409)_TRAVELINITIATE = descriptor.Descriptor(name='TravelInitiate', full_name='EA.Sims4.Network.TravelInitiate', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='zoneId', full_name='EA.Sims4.Network.TravelInitiate.zoneId', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1411, serialized_end=1443)_MOVEINMOVEOUTINFO = descriptor.Descriptor(name='MoveInMoveOutInfo', full_name='EA.Sims4.Network.MoveInMoveOutInfo', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='moving_family_id', full_name='EA.Sims4.Network.MoveInMoveOutInfo.moving_family_id', index=0, number=1, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='is_in_game_evict', full_name='EA.Sims4.Network.MoveInMoveOutInfo.is_in_game_evict', index=1, number=2, type=8, cpp_type=7, label=1, has_default_value=True, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1445, serialized_end=1523)_SELLRETAILLOT = descriptor.Descriptor(name='SellRetailLot', full_name='EA.Sims4.Network.SellRetailLot', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='retail_zone_id', full_name='EA.Sims4.Network.SellRetailLot.retail_zone_id', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1525, serialized_end=1564)_TRAVELSIMSTOZONE = descriptor.Descriptor(name='TravelSimsToZone', full_name='EA.Sims4.Network.TravelSimsToZone', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='zone_id', full_name='EA.Sims4.Network.TravelSimsToZone.zone_id', index=0, number=1, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='sim_ids', full_name='EA.Sims4.Network.TravelSimsToZone.sim_ids', index=1, number=2, type=6, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01')), descriptor.FieldDescriptor(name='active_sim_id', full_name='EA.Sims4.Network.TravelSimsToZone.active_sim_id', index=2, number=3, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1566, serialized_end=1645)_CASAVAILABLEZONESINFO = descriptor.Descriptor(name='CASAvailableZonesInfo', full_name='EA.Sims4.Network.CASAvailableZonesInfo', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='zones', full_name='EA.Sims4.Network.CASAvailableZonesInfo.zones', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1647, serialized_end=1719)_WORLDZONESINFO = descriptor.Descriptor(name='WorldZonesInfo', full_name='EA.Sims4.Network.WorldZonesInfo', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.Network.WorldZonesInfo.name', index=0, number=1, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='defaultName', full_name='EA.Sims4.Network.WorldZonesInfo.defaultName', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='zones', full_name='EA.Sims4.Network.WorldZonesInfo.zones', index=2, number=3, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='worldId', full_name='EA.Sims4.Network.WorldZonesInfo.worldId', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1722, serialized_end=1868)_ZONEINFO = descriptor.Descriptor(name='ZoneInfo', full_name='EA.Sims4.Network.ZoneInfo', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='id', full_name='EA.Sims4.Network.ZoneInfo.id', index=0, number=1, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.Network.ZoneInfo.name', index=1, number=3, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='defaultName', full_name='EA.Sims4.Network.ZoneInfo.defaultName', index=2, number=4, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='world_id', full_name='EA.Sims4.Network.ZoneInfo.world_id', index=3, number=5, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='lot_description_id', full_name='EA.Sims4.Network.ZoneInfo.lot_description_id', index=4, number=7, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=1871, serialized_end=2009)_INTERACTIONPROGRESSUPDATE = descriptor.Descriptor(name='InteractionProgressUpdate', full_name='EA.Sims4.Network.InteractionProgressUpdate', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='sim_id', full_name='EA.Sims4.Network.InteractionProgressUpdate.sim_id', index=0, number=1, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='name', full_name='EA.Sims4.Network.InteractionProgressUpdate.name', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='percent', full_name='EA.Sims4.Network.InteractionProgressUpdate.percent', index=2, number=3, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='rate_change', full_name='EA.Sims4.Network.InteractionProgressUpdate.rate_change', index=3, number=4, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='interaction_id', full_name='EA.Sims4.Network.InteractionProgressUpdate.interaction_id', index=4, number=5, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=2012, serialized_end=2166)_SIMTRANSFERREQUEST = descriptor.Descriptor(name='SimTransferRequest', full_name='EA.Sims4.Network.SimTransferRequest', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='source_household_id', full_name='EA.Sims4.Network.SimTransferRequest.source_household_id', index=0, number=1, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='target_household_id', full_name='EA.Sims4.Network.SimTransferRequest.target_household_id', index=1, number=2, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='active_sim_id', full_name='EA.Sims4.Network.SimTransferRequest.active_sim_id', index=2, number=3, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=2168, serialized_end=2269)_PHONENOTIFICATIONUPDATE = descriptor.Descriptor(name='PhoneNotificationUpdate', full_name='EA.Sims4.Network.PhoneNotificationUpdate', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='interaction_ids', full_name='EA.Sims4.Network.PhoneNotificationUpdate.interaction_ids', index=0, number=1, type=4, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01')), descriptor.FieldDescriptor(name='sim_id', full_name='EA.Sims4.Network.PhoneNotificationUpdate.sim_id', index=1, number=2, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=2271, serialized_end=2341)_INTERACTABLE_INTERACTABLEFLAGS.containing_type = _INTERACTABLE_PIEMENUITEM.fields_by_name['loc_string'].message_type = Localization_pb2._LOCALIZEDSTRING_PIEMENUITEM.fields_by_name['icon'].message_type = ResourceKey_pb2._RESOURCEKEY_PIEMENUITEM.fields_by_name['disabled_text'].message_type = Localization_pb2._LOCALIZEDSTRING_PIEMENUITEM.fields_by_name['score_icon'].message_type = ResourceKey_pb2._RESOURCEKEY_PIEMENUITEM.fields_by_name['icons'].message_type = ResourceKey_pb2._RESOURCEKEY_PIEMENUITEM.fields_by_name['success_tooltip'].message_type = Localization_pb2._LOCALIZEDSTRING_PIEMENUITEM.fields_by_name['icon_infos'].message_type = UI_pb2._ICONINFO_PIEMENUCREATE.fields_by_name['items'].message_type = _PIEMENUITEM_PIEMENUCREATE.fields_by_name['category_tokens'].message_type = Localization_pb2._LOCALIZEDSTRINGTOKEN_PIEMENUCREATE.fields_by_name['disabled_tooltip'].message_type = Localization_pb2._LOCALIZEDSTRING_CASAVAILABLEZONESINFO.fields_by_name['zones'].message_type = _WORLDZONESINFO_WORLDZONESINFO.fields_by_name['defaultName'].message_type = Localization_pb2._LOCALIZEDSTRING_WORLDZONESINFO.fields_by_name['zones'].message_type = _ZONEINFO_ZONEINFO.fields_by_name['defaultName'].message_type = Localization_pb2._LOCALIZEDSTRING_INTERACTIONPROGRESSUPDATE.fields_by_name['name'].message_type = Localization_pb2._LOCALIZEDSTRINGDESCRIPTOR.message_types_by_name['Interactable'] = _INTERACTABLEDESCRIPTOR.message_types_by_name['PieMenuItem'] = _PIEMENUITEMDESCRIPTOR.message_types_by_name['PieMenuCreate'] = _PIEMENUCREATEDESCRIPTOR.message_types_by_name['TravelMenuCreate'] = _TRAVELMENUCREATEDESCRIPTOR.message_types_by_name['TravelMenuInfo'] = _TRAVELMENUINFODESCRIPTOR.message_types_by_name['TravelMenuResponse'] = _TRAVELMENURESPONSEDESCRIPTOR.message_types_by_name['TravelInitiate'] = _TRAVELINITIATEDESCRIPTOR.message_types_by_name['MoveInMoveOutInfo'] = _MOVEINMOVEOUTINFODESCRIPTOR.message_types_by_name['SellRetailLot'] = _SELLRETAILLOTDESCRIPTOR.message_types_by_name['TravelSimsToZone'] = _TRAVELSIMSTOZONEDESCRIPTOR.message_types_by_name['CASAvailableZonesInfo'] = _CASAVAILABLEZONESINFODESCRIPTOR.message_types_by_name['WorldZonesInfo'] = _WORLDZONESINFODESCRIPTOR.message_types_by_name['ZoneInfo'] = _ZONEINFODESCRIPTOR.message_types_by_name['InteractionProgressUpdate'] = _INTERACTIONPROGRESSUPDATEDESCRIPTOR.message_types_by_name['SimTransferRequest'] = _SIMTRANSFERREQUESTDESCRIPTOR.message_types_by_name['PhoneNotificationUpdate'] = _PHONENOTIFICATIONUPDATE
class Interactable(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _INTERACTABLE

class PieMenuItem(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PIEMENUITEM

class PieMenuCreate(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PIEMENUCREATE

class TravelMenuCreate(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _TRAVELMENUCREATE

class TravelMenuInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _TRAVELMENUINFO

class TravelMenuResponse(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _TRAVELMENURESPONSE

class TravelInitiate(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _TRAVELINITIATE

class MoveInMoveOutInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _MOVEINMOVEOUTINFO

class SellRetailLot(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SELLRETAILLOT

class TravelSimsToZone(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _TRAVELSIMSTOZONE

class CASAvailableZonesInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CASAVAILABLEZONESINFO

class WorldZonesInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _WORLDZONESINFO

class ZoneInfo(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _ZONEINFO

class InteractionProgressUpdate(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _INTERACTIONPROGRESSUPDATE

class SimTransferRequest(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _SIMTRANSFERREQUEST

class PhoneNotificationUpdate(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PHONENOTIFICATIONUPDATE
