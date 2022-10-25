from google.protobuf import descriptorfrom google.protobuf import messagefrom google.protobuf import reflectionfrom google.protobuf import descriptor_pb2import protocolbuffers.S4Common_pb2 as S4Common_pb2DESCRIPTOR = descriptor.FileDescriptor(name='Outfits.proto', package='EA.Sims4.Persistence', serialized_pb='\n\rOutfits.proto\x12\x14EA.Sims4.Persistence\x1a\x0eS4Common.proto"\'\n\rBodyTypesList\x12\x16\n\nbody_types\x18\x01 \x03(\rB\x02\x10\x01")\n\x0eColorShiftList\x12\x17\n\x0bcolor_shift\x18\x01 \x03(\x04B\x02\x10\x01"�\x02\n\nOutfitData\x12\x11\n\toutfit_id\x18\x01 \x02(\x04\x12\x10\n\x08category\x18\x02 \x01(\r\x12\x1f\n\x05parts\x18\x05 \x01(\x0b2\x10.EA.Sims4.IdList\x12\x0f\n\x07created\x18\x06 \x01(\x04\x12<\n\x0fbody_types_list\x18\x07 \x01(\x0b2#.EA.Sims4.Persistence.BodyTypesList\x12\x1f\n\x10match_hair_style\x18\t \x01(\x08:\x05false\x12\x14\n\x0coutfit_flags\x18\n \x01(\x04\x12\x1c\n\x11outfit_flags_high\x18\x0b \x01(\x04:\x010\x129\n\x0bpart_shifts\x18\x0c \x01(\x0b2$.EA.Sims4.Persistence.ColorShiftList\x12\r\n\x05title\x18\r \x01(\t"?\n\nOutfitList\x121\n\x07outfits\x18\x01 \x03(\x0b2 .EA.Sims4.Persistence.OutfitData"S\n\x08PartData\x12\n\n\x02id\x18\x01 \x02(\x04\x12\x11\n\tbody_type\x18\x02 \x02(\r\x12(\n\x0bcolor_shift\x18\x03 \x01(\x04:\x134611686018427387904"=\n\x0cPartDataList\x12-\n\x05parts\x18\x01 \x03(\x0b2\x1e.EA.Sims4.Persistence.PartData"�\x01\n\x0bGeneticData\x12\x1d\n\x15sculpts_and_mods_attr\x18\x01 \x01(\x0c\x12\x10\n\x08physique\x18\x02 \x01(\t\x12\x13\n\x0bvoice_pitch\x18\x03 \x01(\x02\x12\x13\n\x0bvoice_actor\x18\x04 \x01(\r\x126\n\nparts_list\x18\x05 \x01(\x0b2".EA.Sims4.Persistence.PartDataList\x12=\n\x11growth_parts_list\x18\x06 \x01(\x0b2".EA.Sims4.Persistence.PartDataList"0\n\rPeltLayerData\x12\x10\n\x08layer_id\x18\x01 \x01(\x04\x12\r\n\x05color\x18\x02 \x01(\r"H\n\x11PeltLayerDataList\x123\n\x06layers\x18\x01 \x03(\x0b2#.EA.Sims4.Persistence.PeltLayerData')_BODYTYPESLIST = descriptor.Descriptor(name='BodyTypesList', full_name='EA.Sims4.Persistence.BodyTypesList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='body_types', full_name='EA.Sims4.Persistence.BodyTypesList.body_types', index=0, number=1, type=13, cpp_type=3, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01'))], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=55, serialized_end=94)_COLORSHIFTLIST = descriptor.Descriptor(name='ColorShiftList', full_name='EA.Sims4.Persistence.ColorShiftList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='color_shift', full_name='EA.Sims4.Persistence.ColorShiftList.color_shift', index=0, number=1, type=4, cpp_type=4, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\x10\x01'))], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=96, serialized_end=137)_OUTFITDATA = descriptor.Descriptor(name='OutfitData', full_name='EA.Sims4.Persistence.OutfitData', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='outfit_id', full_name='EA.Sims4.Persistence.OutfitData.outfit_id', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='category', full_name='EA.Sims4.Persistence.OutfitData.category', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='parts', full_name='EA.Sims4.Persistence.OutfitData.parts', index=2, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='created', full_name='EA.Sims4.Persistence.OutfitData.created', index=3, number=6, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='body_types_list', full_name='EA.Sims4.Persistence.OutfitData.body_types_list', index=4, number=7, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='match_hair_style', full_name='EA.Sims4.Persistence.OutfitData.match_hair_style', index=5, number=9, type=8, cpp_type=7, label=1, has_default_value=True, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='outfit_flags', full_name='EA.Sims4.Persistence.OutfitData.outfit_flags', index=6, number=10, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='outfit_flags_high', full_name='EA.Sims4.Persistence.OutfitData.outfit_flags_high', index=7, number=11, type=4, cpp_type=4, label=1, has_default_value=True, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='part_shifts', full_name='EA.Sims4.Persistence.OutfitData.part_shifts', index=8, number=12, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='title', full_name='EA.Sims4.Persistence.OutfitData.title', index=9, number=13, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=140, serialized_end=460)_OUTFITLIST = descriptor.Descriptor(name='OutfitList', full_name='EA.Sims4.Persistence.OutfitList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='outfits', full_name='EA.Sims4.Persistence.OutfitList.outfits', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=462, serialized_end=525)_PARTDATA = descriptor.Descriptor(name='PartData', full_name='EA.Sims4.Persistence.PartData', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='id', full_name='EA.Sims4.Persistence.PartData.id', index=0, number=1, type=4, cpp_type=4, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='body_type', full_name='EA.Sims4.Persistence.PartData.body_type', index=1, number=2, type=13, cpp_type=3, label=2, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='color_shift', full_name='EA.Sims4.Persistence.PartData.color_shift', index=2, number=3, type=4, cpp_type=4, label=1, has_default_value=True, default_value=4611686018427387904, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=527, serialized_end=610)_PARTDATALIST = descriptor.Descriptor(name='PartDataList', full_name='EA.Sims4.Persistence.PartDataList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='parts', full_name='EA.Sims4.Persistence.PartDataList.parts', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=612, serialized_end=673)_GENETICDATA = descriptor.Descriptor(name='GeneticData', full_name='EA.Sims4.Persistence.GeneticData', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='sculpts_and_mods_attr', full_name='EA.Sims4.Persistence.GeneticData.sculpts_and_mods_attr', index=0, number=1, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b'', message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='physique', full_name='EA.Sims4.Persistence.GeneticData.physique', index=1, number=2, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='voice_pitch', full_name='EA.Sims4.Persistence.GeneticData.voice_pitch', index=2, number=3, type=2, cpp_type=6, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='voice_actor', full_name='EA.Sims4.Persistence.GeneticData.voice_actor', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='parts_list', full_name='EA.Sims4.Persistence.GeneticData.parts_list', index=4, number=5, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='growth_parts_list', full_name='EA.Sims4.Persistence.GeneticData.growth_parts_list', index=5, number=6, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=676, serialized_end=899)_PELTLAYERDATA = descriptor.Descriptor(name='PeltLayerData', full_name='EA.Sims4.Persistence.PeltLayerData', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='layer_id', full_name='EA.Sims4.Persistence.PeltLayerData.layer_id', index=0, number=1, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='color', full_name='EA.Sims4.Persistence.PeltLayerData.color', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=901, serialized_end=949)_PELTLAYERDATALIST = descriptor.Descriptor(name='PeltLayerDataList', full_name='EA.Sims4.Persistence.PeltLayerDataList', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='layers', full_name='EA.Sims4.Persistence.PeltLayerDataList.layers', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=951, serialized_end=1023)_OUTFITDATA.fields_by_name['parts'].message_type = S4Common_pb2._IDLIST_OUTFITDATA.fields_by_name['body_types_list'].message_type = _BODYTYPESLIST_OUTFITDATA.fields_by_name['part_shifts'].message_type = _COLORSHIFTLIST_OUTFITLIST.fields_by_name['outfits'].message_type = _OUTFITDATA_PARTDATALIST.fields_by_name['parts'].message_type = _PARTDATA_GENETICDATA.fields_by_name['parts_list'].message_type = _PARTDATALIST_GENETICDATA.fields_by_name['growth_parts_list'].message_type = _PARTDATALIST_PELTLAYERDATALIST.fields_by_name['layers'].message_type = _PELTLAYERDATADESCRIPTOR.message_types_by_name['BodyTypesList'] = _BODYTYPESLISTDESCRIPTOR.message_types_by_name['ColorShiftList'] = _COLORSHIFTLISTDESCRIPTOR.message_types_by_name['OutfitData'] = _OUTFITDATADESCRIPTOR.message_types_by_name['OutfitList'] = _OUTFITLISTDESCRIPTOR.message_types_by_name['PartData'] = _PARTDATADESCRIPTOR.message_types_by_name['PartDataList'] = _PARTDATALISTDESCRIPTOR.message_types_by_name['GeneticData'] = _GENETICDATADESCRIPTOR.message_types_by_name['PeltLayerData'] = _PELTLAYERDATADESCRIPTOR.message_types_by_name['PeltLayerDataList'] = _PELTLAYERDATALIST
class BodyTypesList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _BODYTYPESLIST

class ColorShiftList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _COLORSHIFTLIST

class OutfitData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _OUTFITDATA

class OutfitList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _OUTFITLIST

class PartData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PARTDATA

class PartDataList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PARTDATALIST

class GeneticData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _GENETICDATA

class PeltLayerData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PELTLAYERDATA

class PeltLayerDataList(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _PELTLAYERDATALIST
