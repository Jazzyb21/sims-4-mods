from _weakrefset import WeakSetfrom collections import defaultdictimport sims4from sims4.service_manager import Servicelogger = sims4.log.Logger('Zone Reservation', default_owner='rrodgers')
class ZoneReservationService(Service):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._reserved_zones = defaultdict(WeakSet)

    def start(self):
        return True

    def on_zone_load(self):
        pass

    def on_zone_unload(self):
        pass

    def stop(self):
        pass

    def is_reserved(self, zone_id):
        reservations = self._reserved_zones.get(zone_id, None)
        return bool(reservations and len(reservations))

    def reserve_zone(self, reserver, zone_id):
        current_reservations = self._reserved_zones.get(zone_id, None)
        if current_reservations and reserver in current_reservations:
            logger.warn('Zone with id {} is being reserved by {} which already has a reservation for it.', zone_id, reserver)
            return
        self._reserved_zones[zone_id].add(reserver)

    def unreserve_zone(self, reserver, zone_id):
        current_reservations = self._reserved_zones.get(zone_id, None)
        if not current_reservations:
            logger.warn("Trying to unreserve a zone that isn't reserved")
            return
        if reserver not in current_reservations:
            logger.warn('{} is trying to unreserve a zone ({}) but no reservation was found', reserver, zone_id)
            return
        current_reservations.remove(reserver)
        if not current_reservations:
            del self._reserved_zones[zone_id]
