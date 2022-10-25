from routing.waypoints.waypoint_generator_connected_points import _WaypointGeneratorConnectedPointsfrom routing.waypoints.waypoint_generator_ellipse import _WaypointGeneratorEllipsefrom routing.waypoints.waypoint_generator_footprint import _WaypointGeneratorFootprintfrom routing.waypoints.waypoint_generator_lot import _WaypointGeneratorLotPointsfrom routing.waypoints.waypoint_generator_pacing import _WaypointGeneratorPacingfrom routing.waypoints.waypoint_generator_points import _WaypointGeneratorObjectPointsfrom routing.waypoints.waypoint_generator_pool import _WaypointGeneratorPoolfrom routing.waypoints.waypoint_generator_spawn_points import _WaypointGeneratorSpawnPointsfrom routing.waypoints.waypoint_generator_tags import _WaypointGeneratorMultipleObjectByTagfrom routing.waypoints.waypoint_generator_unobstructed_line import _WaypointGeneratorUnobstructedLinefrom routing.waypoints.waypoint_generator_gig_objects import _WaypointGeneratorMultipleGigObjectsfrom sims4.tuning.tunable import TunableVariant
class TunableWaypointGeneratorVariant(TunableVariant):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, description='\n            Define how the waypoints are generated.\n            ', spawn_points=_WaypointGeneratorSpawnPoints.TunableFactory(), lot_points=_WaypointGeneratorLotPoints.TunableFactory(), pool_laps=_WaypointGeneratorPool.TunableFactory(), object_points=_WaypointGeneratorObjectPoints.TunableFactory(), pacing=_WaypointGeneratorPacing.TunableFactory(), multiple_objects_by_tag=_WaypointGeneratorMultipleObjectByTag.TunableFactory(), ellipse=_WaypointGeneratorEllipse.TunableFactory(), footprint=_WaypointGeneratorFootprint.TunableFactory(), unobstructed_line=_WaypointGeneratorUnobstructedLine.TunableFactory(), connected_points=_WaypointGeneratorConnectedPoints.TunableFactory(), gig_objects=_WaypointGeneratorMultipleGigObjects.TunableFactory(), default='spawn_points', **kwargs)
