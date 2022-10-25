import services
class TempleUtils:

    @classmethod
    def get_temple_zone_director(cls):
        venue_service = services.venue_service()
        if venue_service is None:
            return
        else:
            zone_director = venue_service.get_zone_director()
            if hasattr(zone_director, '_temple_data'):
                return zone_director
