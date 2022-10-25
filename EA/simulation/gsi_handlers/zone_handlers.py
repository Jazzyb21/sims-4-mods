import services
@GsiHandler('zone_view', zone_view_schema)
def generate_zone_view_data():
    zone_list = []
    for zone in services._zone_manager.objects:
        if zone.is_instantiated:
            zone_list.append({'zoneId': hex(zone.id), 'zoneName': 'ZoneName'})
    return zone_list
