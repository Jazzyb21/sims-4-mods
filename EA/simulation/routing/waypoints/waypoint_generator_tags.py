from routing.waypoints.waypoint_generator_object_mixin import _WaypointGeneratorMultipleObjectMixinfrom tag import TunableTagsimport services
class _WaypointGeneratorMultipleObjectByTag(_WaypointGeneratorMultipleObjectMixin):
    FACTORY_TUNABLES = {'object_tags': TunableTags(description='\n            Find all of the objects based on these tags.\n            ', filter_prefixes=('func',))}

    def _get_objects(self):
        return services.object_manager().get_objects_matching_tags(self.object_tags, match_any=True)
