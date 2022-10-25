from google.protobuf import descriptorfrom google.protobuf import messagefrom google.protobuf import reflectionfrom google.protobuf import descriptor_pb2import protocolbuffers.SimObjectAttributes_pb2 as SimObjectAttributes_pb2DESCRIPTOR = descriptor.FileDescriptor(name='Venue.proto', package='EA.Sims4.Network', serialized_pb='\n\x0bVenue.proto\x12\x10EA.Sims4.Network\x1a\x19SimObjectAttributes.proto"b\n\x0cCareerOutfit\x12\x17\n\x0coutfit_index\x18\x01 \x02(\r:\x010\x129\n\tmannequin\x18\x02 \x01(\x0b2&.EA.Sims4.Persistence.MannequinSimData"\x88\x01\n\x16VetClinicConfiguration\x12/\n\x07outfits\x18\x01 \x03(\x0b2\x1e.EA.Sims4.Network.CareerOutfit"=\n\x13VetClinicOutfitType\x12\x11\n\rMALE_EMPLOYEE\x10\x00\x12\x13\n\x0fFEMALE_EMPLOYEE\x10\x01"\x8d\x01\n\x1eUniversityHousingConfiguration\x12\x15\n\runiversity_id\x18\x01 \x01(\x04\x12\x0e\n\x06gender\x18\x02 \x01(\r\x12\x17\n\x0forganization_id\x18\x03 \x01(\x04\x12\x1a\n\x12roommate_bed_count\x18\x04 \x01(\r\x12\x0f\n\x07club_id\x18\x06 \x01(\x04"I\n\x12VenueUpdateRequest\x12\x11\n\tvenue_key\x18\x01 \x01(\x06\x12\x0e\n\x06lot_id\x18\x02 \x01(\r\x12\x10\n\x08world_id\x18\x03 \x01(\r')_VETCLINICCONFIGURATION_VETCLINICOUTFITTYPE = descriptor.EnumDescriptor(name='VetClinicOutfitType', full_name='EA.Sims4.Network.VetClinicConfiguration.VetClinicOutfitType', filename=None, file=DESCRIPTOR, values=[descriptor.EnumValueDescriptor(name='MALE_EMPLOYEE', index=0, number=0, options=None, type=None), descriptor.EnumValueDescriptor(name='FEMALE_EMPLOYEE', index=1, number=1, options=None, type=None)], containing_type=None, options=None, serialized_start=236, serialized_end=297)_CAREEROUTFIT = descriptor.Descriptor(name='CareerOutfit', full_name='EA.Sims4.Network.CareerOutfit', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='outfit_index', full_name='EA.Sims4.Network.CareerOutfit.outfit_index', index=0, number=1, type=13, cpp_type=3, label=2, has_default_value=True, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='mannequin', full_name='EA.Sims4.Network.CareerOutfit.mannequin', index=1, number=2, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=60, serialized_end=158)_VETCLINICCONFIGURATION = descriptor.Descriptor(name='VetClinicConfiguration', full_name='EA.Sims4.Network.VetClinicConfiguration', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='outfits', full_name='EA.Sims4.Network.VetClinicConfiguration.outfits', index=0, number=1, type=11, cpp_type=10, label=3, has_default_value=False, default_value=[], message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[_VETCLINICCONFIGURATION_VETCLINICOUTFITTYPE], options=None, is_extendable=False, extension_ranges=[], serialized_start=161, serialized_end=297)_UNIVERSITYHOUSINGCONFIGURATION = descriptor.Descriptor(name='UniversityHousingConfiguration', full_name='EA.Sims4.Network.UniversityHousingConfiguration', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='university_id', full_name='EA.Sims4.Network.UniversityHousingConfiguration.university_id', index=0, number=1, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='gender', full_name='EA.Sims4.Network.UniversityHousingConfiguration.gender', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='organization_id', full_name='EA.Sims4.Network.UniversityHousingConfiguration.organization_id', index=2, number=3, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='roommate_bed_count', full_name='EA.Sims4.Network.UniversityHousingConfiguration.roommate_bed_count', index=3, number=4, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='club_id', full_name='EA.Sims4.Network.UniversityHousingConfiguration.club_id', index=4, number=6, type=4, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=300, serialized_end=441)_VENUEUPDATEREQUEST = descriptor.Descriptor(name='VenueUpdateRequest', full_name='EA.Sims4.Network.VenueUpdateRequest', filename=None, file=DESCRIPTOR, containing_type=None, fields=[descriptor.FieldDescriptor(name='venue_key', full_name='EA.Sims4.Network.VenueUpdateRequest.venue_key', index=0, number=1, type=6, cpp_type=4, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='lot_id', full_name='EA.Sims4.Network.VenueUpdateRequest.lot_id', index=1, number=2, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None), descriptor.FieldDescriptor(name='world_id', full_name='EA.Sims4.Network.VenueUpdateRequest.world_id', index=2, number=3, type=13, cpp_type=3, label=1, has_default_value=False, default_value=0, message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, options=None)], extensions=[], nested_types=[], enum_types=[], options=None, is_extendable=False, extension_ranges=[], serialized_start=443, serialized_end=516)_CAREEROUTFIT.fields_by_name['mannequin'].message_type = SimObjectAttributes_pb2._MANNEQUINSIMDATA_VETCLINICCONFIGURATION.fields_by_name['outfits'].message_type = _CAREEROUTFIT_VETCLINICCONFIGURATION_VETCLINICOUTFITTYPE.containing_type = _VETCLINICCONFIGURATIONDESCRIPTOR.message_types_by_name['CareerOutfit'] = _CAREEROUTFITDESCRIPTOR.message_types_by_name['VetClinicConfiguration'] = _VETCLINICCONFIGURATIONDESCRIPTOR.message_types_by_name['UniversityHousingConfiguration'] = _UNIVERSITYHOUSINGCONFIGURATIONDESCRIPTOR.message_types_by_name['VenueUpdateRequest'] = _VENUEUPDATEREQUEST
class CareerOutfit(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _CAREEROUTFIT

class VetClinicConfiguration(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _VETCLINICCONFIGURATION

class UniversityHousingConfiguration(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _UNIVERSITYHOUSINGCONFIGURATION

class VenueUpdateRequest(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _VENUEUPDATEREQUEST
