from google.protobuf import descriptorfrom google.protobuf import messagefrom google.protobuf import reflectionfrom google.protobuf import descriptor_pb2DESCRIPTOR = descriptor.FileDescriptor(name='Vehicles.proto', package='EA.Sims4.Network', serialized_pb='\n\x0eVehicles.proto\x12\x10EA.Sims4.Network"\x94\x02\n\x0eVehicleControl\x12\x12\n\ncontrol_id\x18\x01 \x01(\r\x12I\n\x0ccontrol_type\x18\x02 \x01(\x0e23.EA.Sims4.Network.VehicleControl.VehicleControlType\x12\x17\n\x0fjoint_name_hash\x18\x03 \x01(\r\x12!\n\x19reference_joint_name_hash\x18\x04 \x01(\r\x12 \n\x18enable_terrain_alignment\x18\x05 \x01(\x08\x12\x17\n\x0fbump_sound_name\x18\x06 \x01(\t",\n\x12VehicleControlType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05WHEEL\x10\x01"A\n\x0bVehicleData\x122\n\x08controls\x18\x01 \x03(\x0b2 .EA.Sims4.Network.VehicleControl')_VEHICLECONTROL_VEHICLECONTROLTYPE = descriptor.EnumDescriptor(name='VehicleControlType', full_name='EA.Sims4.Network.VehicleControl.VehicleControlType', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='UNKNOWN', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='WHEEL', index=1, number=1, options=None, type=None)], containing_type=None, options=None, serialized_start=269, serialized_end=313)_VEHICLECONTROL = descriptor.Descriptor(name='VehicleControl', full_name='EA.Sims4.Network.VehicleControl', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='control_id', full_name='EA.Sims4.Network.VehicleControl.control_id', index=0, number=1, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='control_type', full_name='EA.Sims4.Network.VehicleControl.control_type', index=1, number=2, type=14, cpp_type=8, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='joint_name_hash', full_name='EA.Sims4.Network.VehicleControl.joint_name_hash', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='reference_joint_name_hash', full_name='EA.Sims4.Network.VehicleControl.reference_joint_name_hash', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='enable_terrain_alignment', full_name='EA.Sims4.Network.VehicleControl.enable_terrain_alignment', index=4, number=5, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='bump_sound_name', full_name='EA.Sims4.Network.VehicleControl.bump_sound_name', index=5, number=6, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_VEHICLECONTROL_VEHICLECONTROLTYPE], options=None, is_extendable=False, extension_ranges=[], serialized_start=37, serialized_end=313)_VEHICLEDATA = descriptor.Descriptor(name='VehicleData', full_name='EA.Sims4.Network.VehicleData', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='controls', full_name='EA.Sims4.Network.VehicleData.controls', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=315, serialized_end=380)_VEHICLECONTROL.fields_by_name['control_type'].enum_type = _VEHICLECONTROL_VEHICLECONTROLTYPE_VEHICLECONTROL_VEHICLECONTROLTYPE.containing_type = _VEHICLECONTROL_VEHICLEDATA.fields_by_name['controls'].message_type = _VEHICLECONTROLDESCRIPTOR.message_types_by_name['VehicleControl'] = _VEHICLECONTROLDESCRIPTOR.message_types_by_name['VehicleData'] = _VEHICLEDATA
class VehicleControl(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _VEHICLECONTROL

class VehicleData(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _VEHICLEDATA
