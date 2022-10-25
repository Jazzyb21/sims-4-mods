from collections import OrderedDict, namedtuple, defaultdictfrom contextlib import contextmanagerimport collectionsimport functoolsimport itertoolsimport operatorimport timeimport weakrefimport xml.etreefrom caches import BarebonesCachefrom event_testing.resolver import SingleActorAndObjectResolverfrom objects.pools.pond_utils import PondUtilsfrom routing.path_planner.height_clearance_helper import get_required_height_clearancefrom sims4 import reloadfrom sims4.callback_utils import CallableTestListfrom sims4.collections import frozendict, enumdictfrom sims4.geometry import test_point_in_compound_polygon, QtCirclefrom sims4.log import Logger, StackVarfrom sims4.repr_utils import standard_angle_repr, suppress_quotesfrom sims4.service_manager import Servicefrom sims4.sim_irq_service import yield_to_irqfrom sims4.tuning.geometric import TunableVector2from sims4.tuning.tunable import Tunable, TunableReference, TunableList, TunableMapping, TunableEnumEntryfrom sims4.utils import enumerate_reversedfrom singletons import DEFAULTimport algosimport cachesimport enumimport sims4.geometryimport sims4.mathimport sims4.reloadfrom animation.posture_manifest import SlotManifestEntry, AnimationParticipantfrom animation.posture_manifest_constants import SWIM_AT_NONE_CONSTRAINT, STAND_AT_NONE_CONSTRAINTfrom autonomy.autonomy_preference import AutonomyPreferenceTypefrom balloon.passive_balloons import PassiveBalloonsfrom element_utils import build_element, maybefrom event_testing.results import TestResultfrom indexed_manager import CallbackTypesfrom interactions import ParticipantType, constraintsfrom interactions.aop import AffordanceObjectPairfrom interactions.constraints import create_transform_geometry, Anywhere, ANYWHERE, RequiredSlotSingle, create_constraint_set, Constraint, Nowherefrom interactions.context import InteractionContext, QueueInsertStrategy, InteractionSourcefrom interactions.interaction_finisher import FinishingTypefrom interactions.priority import Priorityfrom interactions.utils import routing_constantsfrom interactions.utils.interaction_liabilities import RESERVATION_LIABILITY, ReservationLiabilityfrom interactions.utils.routing import FollowPath, get_route_element_for_path, SlotGoalfrom interactions.utils.routing_constants import TransitionFailureReasonsfrom objects import ALL_HIDDEN_REASONSfrom objects.definition import Definitionfrom objects.helpers.user_footprint_helper import push_route_awayfrom objects.object_enums import ResetReasonfrom objects.pools import pool_utilsfrom objects.proxy import ProxyObjectfrom postures import DerailReasonfrom postures.base_postures import create_puppet_posturesfrom postures.generic_posture_node import SimPostureNodefrom postures.posture import Posturefrom postures.posture_errors import PostureGraphError, PostureGraphMiddlePathErrorfrom postures.posture_scoring import PostureScoring, may_reserve_posture_targetfrom postures.posture_specs import PostureSpecVariable, PostureSpec, PostureOperation, get_origin_spec, get_origin_spec_carry, with_caches, get_pick_up_spec_sequence, get_put_down_spec_sequence, destination_test, PostureAspectBody, PostureAspectSurface, _object_addition, PostureAspectBody_createfrom postures.posture_state_spec import create_body_posture_state_specfrom postures.posture_tuning import PostureTuningfrom relationships.global_relationship_tuning import RelationshipGlobalTuningfrom reservation.reservation_handler_multi import ReservationHandlerMultifrom routing import SurfaceType, GoalFailureTypefrom routing.formation.formation_tuning import FormationTuningfrom routing.formation.formation_type_base import FormationRoutingTypefrom sims.sim_info_types import Speciesfrom world.ocean_tuning import OceanTuningimport build_buyimport cythonimport debugvisimport element_utilsimport elementsimport event_testing.test_utilsimport gsi_handlers.posture_graph_handlersimport indexed_managerimport interactions.utils.routingimport posturesimport primitives.routing_utilsimport routingimport servicesimport terrainif not cython.compiled:
    from postures.posture_specs import get_origin_spec, get_origin_spec_carry, PostureSpec, PostureAspectBody
    import cython_utils as cuMAX_RIGHT_PATHS = 30NON_OPTIMAL_PATH_DESTINATION = 1000logger = Logger('PostureGraph')cython_log = Logger('CythonConfig')if cython.compiled:
    cython_log.always('CYTHON posture_graph is imported!', color=sims4.log.LEVEL_WARN)
else:
    cython_log.always('Pure Python posture_graph is imported!', color=sims4.log.LEVEL_WARN)with sims4.reload.protected(globals()):
    SIM_DEFAULT_POSTURE_TYPE = None
    SIM_DEFAULT_AOPS = None
    SIM_DEFAULT_OPERATION = None
    STAND_AT_NONE = None
    STAND_AT_NONE_CARRY = None
    STAND_AT_NONE_NODES = None
    SIM_SWIM_POSTURE_TYPE = None
    SIM_SWIM_AOPS = None
    SIM_SWIM_OPERATION = None
    SWIM_AT_NONE = None
    SWIM_AT_NONE_CARRY = None
    SWIM_AT_NONE_NODES = None
    _MOBILE_NODES_AT_NONE = None
    _MOBILE_NODES_AT_NONE_CARRY = None
    _DEFAULT_MOBILE_NODES = None
    enable_debug_goals_visualization = False
    on_transition_destinations_changed = sims4.callback_utils.CallableList()InsertionIndexAndSpec = namedtuple('InsertionIndexAndSpec', ['index', 'spec'])
@cython.cfunc
@cython.exceptval(check=False)
def get_subset_keys(node_or_spec:PostureSpec) -> set:
    keys = set()
    posture_type = node_or_spec.get_body_posture()
    if posture_type is not None:
        keys.add(('posture_type', posture_type))
    carry_target = node_or_spec.get_carry_target()
    keys.add(('carry_target', carry_target))
    body_target = node_or_spec.body_target
    body_target = getattr(body_target, 'part_owner', None) or body_target
    if node_or_spec.surface is not None:
        original_surface_target = node_or_spec.get_surface_target()
        surface_target = getattr(original_surface_target, 'part_owner', None) or original_surface_target
        keys.add(('slot_target', node_or_spec.get_slot_target()))
        slot_type = node_or_spec.get_slot_type()
        if slot_type is not None and slot_type != PostureSpecVariable.SLOT:
            keys.add(('slot_type', slot_type))
        if surface_target == PostureSpecVariable.CONTAINER_TARGET:
            surface_target = node_or_spec.get_body_target()
        if surface_target is None:
            if body_target is not None and (isinstance(body_target, PostureSpecVariable) or body_target.is_surface()):
                keys.add(('surface_target', body_target))
                keys.add(('has_a_surface', True))
            else:
                keys.add(('has_a_surface', False))
        elif surface_target not in (PostureSpecVariable.ANYTHING, PostureSpecVariable.SURFACE_TARGET):
            keys.add(('surface_target', surface_target))
            keys.add(('has_a_surface', True))
        elif surface_target == PostureSpecVariable.SURFACE_TARGET:
            keys.add(('has_a_surface', True))
        if not isinstance(original_surface_target, PostureSpecVariable):
            for slot_type in original_surface_target.get_provided_slot_types():
                keys.add(('slot_type', slot_type))
    else:
        surface_target = None
    if posture_type is not None:
        if body_target != PostureSpecVariable.ANYTHING:
            keys.add(('body_target', body_target))
            if body_target != PostureSpecVariable.BODY_TARGET_FILTERED:
                keys.add(('body_target', PostureSpecVariable.BODY_TARGET_FILTERED))
        elif surface_target is None and posture_type.mobile:
            keys.add(('body_target', None))
    if ('body_target', None) in keys and ('slot_target', None) in keys:
        keys.add(('body_target and slot_target', None))
    return keys

def set_transition_destinations(sim, source_goals, destination_goals, selected_source=None, selected_destination=None, preserve=False, draw_both_sets=False):
    if False and on_transition_destinations_changed:
        transition_destinations = []
        transition_sources = []
        max_dest_cost = 0
        for slot_goal in source_goals:
            slot_transform = sims4.math.Transform(slot_goal.location.position, slot_goal.location.orientation)
            slot_constraint = interactions.constraints.Transform(slot_transform, routing_surface=slot_goal.routing_surface_id)
            if slot_goal is selected_source:
                slot_constraint.was_selected = True
            else:
                slot_constraint.was_selected = False
            transition_sources.append(slot_constraint)
        for slot_goal in destination_goals:
            if slot_goal.cost > max_dest_cost:
                max_dest_cost = slot_goal.cost
            slot_transform = sims4.math.Transform(slot_goal.location.position, slot_goal.location.orientation)
            slot_constraint = interactions.constraints.Transform(slot_transform, routing_surface=slot_goal.routing_surface_id)
            if slot_goal is selected_destination:
                slot_constraint.was_selected = True
            else:
                slot_constraint.was_selected = False
            transition_destinations.append((slot_goal.path_id, slot_constraint, slot_goal.cost))
        on_transition_destinations_changed(sim, transition_destinations, transition_sources, max_dest_cost, preserve=preserve)

def _is_sim_carry(interaction, sim):
    if sim.parent is not None:
        return True
    if interaction.carry_target is sim:
        return True
    if interaction.is_putdown and interaction.target is sim:
        return True
    elif interaction.is_social and interaction.target is sim and interaction.sim is sim.parent:
        return True
    return False

class DistanceEstimator:

    def __init__(self, posture_service, sim, interaction, constraint):
        self.posture_service = posture_service
        self.sim = sim
        self.interaction = interaction
        preferred_objects = interaction.preferred_objects
        self.preferred_objects = preferred_objects
        self.constraint = constraint
        routing_context = sim.get_routing_context()

        @caches.BarebonesCache
        def estimate_connectivity_distance(locations):
            (source_location, dest_location) = locations
            source_locations = ((source_location.transform.translation, source_location.routing_surface),)
            dest_locations = ((dest_location.transform.translation, dest_location.routing_surface),)
            try:
                distance = primitives.routing_utils.estimate_distance_between_multiple_points(source_locations, dest_locations, routing_context)
            except Exception as e:
                logger.warn('{}', e, owner='camilogarcia', trigger_breakpoint=True)
                distance = None
            distance = cu.MAX_FLOAT if distance is None else distance
            return distance

        self.estimate_distance = estimate_distance = estimate_connectivity_distance

        @caches.BarebonesCache
        def get_preferred_object_cost(obj):
            return postures.posture_scoring.PostureScoring.get_preferred_object_cost((obj,), preferred_objects)

        self.get_preferred_object_cost = get_preferred_object_cost

        @caches.BarebonesCache
        def get_inventory_distance(sim_location_inv_node_location_and_mobile):
            cython.declare(node_body_posture_is_mobile=cython.bint)
            (sim_location, inv, node_location, node_body_posture_is_mobile) = sim_location_inv_node_location_and_mobile
            min_dist = cu.MAX_FLOAT
            include_node_location = not node_body_posture_is_mobile or sim_location != node_location
            for owner in inv.owning_objects_gen():
                (routing_position, _) = Constraint.get_validated_routing_position(owner)
                routing_location = routing.Location(routing_position, orientation=owner.orientation, routing_surface=owner.routing_surface)
                distance = cython.cast(cython.double, estimate_distance((sim_location, routing_location)))
                if distance >= min_dist:
                    pass
                else:
                    distance += cython.cast(cython.double, get_preferred_object_cost(owner))
                    if distance >= min_dist:
                        pass
                    else:
                        if include_node_location:
                            distance += cython.cast(cython.double, estimate_distance((routing_location, node_location)))
                        if distance < min_dist:
                            min_dist = distance
            return min_dist

        self.get_inventory_distance = get_inventory_distance

        @caches.BarebonesCache
        def estimate_location_distance(sim_location_and_target_location_and_mobile):
            (sim_location, target_location, node_body_posture_is_mobile) = sim_location_and_target_location_and_mobile
            if interaction.target is None:
                return estimate_distance((sim_location, target_location))
            carry_target = interaction.carry_target
            if carry_target is None:
                return estimate_distance((sim_location, target_location))
            inv = interaction.target.get_inventory()
            if inv is None:
                interaction_target_routing_location = interaction.target.routing_location
                if interaction_target_routing_location == target_location:
                    return estimate_distance((sim_location, target_location))
                if interaction_target_routing_location.routing_surface.type == SurfaceType.SURFACETYPE_OBJECT:
                    interaction_target_world_routing_location = interaction_target_routing_location.get_world_surface_location()
                else:
                    interaction_target_world_routing_location = None
                if interaction.is_put_in_inventory and node_body_posture_is_mobile and sim_location == target_location:
                    distance = estimate_distance((sim_location, interaction_target_routing_location))
                    if interaction_target_world_routing_location is not None:
                        world_distance = estimate_distance((sim_location, interaction_target_world_routing_location))
                        distance = min(distance, world_distance)
                    return distance
                distance = estimate_distance((sim_location, interaction_target_routing_location)) + estimate_distance((interaction_target_routing_location, target_location))
                if interaction_target_world_routing_location is not None:
                    world_distance = estimate_distance((sim_location, interaction_target_world_routing_location)) + estimate_distance((interaction_target_world_routing_location, target_location))
                    distance = min(distance, world_distance)
                return distance
            if inv.owner.is_sim:
                if inv.owner is not sim:
                    return NON_OPTIMAL_PATH_DESTINATION
                return estimate_distance((sim_location, target_location))
            return get_inventory_distance((sim_location, inv, target_location, node_body_posture_is_mobile))

        self.estimate_location_distance = estimate_location_distance

class PathType(enum.Int, export=False):
    LEFT = 0
    MIDDLE_LEFT = 1
    MIDDLE_RIGHT = 2
    RIGHT = 3

class SegmentedPath:

    def __init__(self, posture_graph, sim, source, destination_specs, var_map, constraint, valid_edge_test, interaction, is_complete=True, distance_estimator=None):
        self.posture_graph = posture_graph
        self.sim = sim
        self.interaction = interaction
        self.source = source
        self.valid_edge_test = valid_edge_test
        self.var_map = var_map
        self._var_map_resolved = None
        self.constraint = constraint
        self.is_complete = is_complete
        if is_complete:
            is_sim_carry = _is_sim_carry(interaction, sim)
            source_body_target = source.body_target
            if is_sim_carry:
                destination_specs = dict(destination_specs)
            elif source_body_target is None:
                destination_specs = {dest: spec for (dest, spec) in destination_specs.items() if dest.body_target is None}
            else:
                if source_body_target.is_part:
                    source_body_target = source_body_target.part_owner
                destination_specs = {dest: spec for (dest, spec) in destination_specs.items() if source_body_target.is_same_object_or_part(dest.body_target)}
        if not destination_specs:
            raise ValueError('Segmented paths need destinations.')
        self.destination_specs = destination_specs
        self.destinations = destination_specs.keys()
        if distance_estimator is None:
            distance_estimator = DistanceEstimator(self.posture_graph, self.sim, self.interaction, constraint)
        self._distance_estimator = distance_estimator

    def teardown(self):
        pass

    @property
    def var_map_resolved(self):
        if self._var_map_resolved is None:
            return self.var_map
        return self._var_map_resolved

    @var_map_resolved.setter
    def var_map_resolved(self, value):
        self._var_map_resolved = value

    def check_validity(self, sim):
        source_spec = sim.posture_state.get_posture_spec(self.var_map)
        return source_spec == self.source

    def generate_left_paths(self):
        left_path_gen = self.posture_graph._left_path_gen(self.sim, self.source, self.destinations, self.interaction, self.constraint, self.var_map, self.valid_edge_test, is_complete=self.is_complete)
        for path_left in left_path_gen:
            path_left.segmented_path = self
            yield path_left

    def generate_right_paths(self, sim, path_left):
        if path_left[-1] in self.destinations and len(self.destinations) == 1:
            cost = self.posture_graph._get_goal_cost(self.sim, self.interaction, self.constraint, self.var_map, path_left[-1])
            path_right = algos.Path([path_left[-1]], cost)
            path_right.segmented_path = self
            yield path_right
            return
        allow_carried = False
        if self.is_complete:
            left_destinations = (path_left[-1],)
        else:
            carry = self.var_map.get(PostureSpecVariable.CARRY_TARGET)
            if carry is sim:
                left_destinations = (path_left[-1],)
                allow_carried = True
            else:
                for constraint in self.constraint:
                    if not constraint.posture_state_spec is not None or not carry is not self.sim or constraint.posture_state_spec.references_object(carry):
                        break
                carry = None
                if carry is not None and path_left[-1].carry_target is None and carry is None or isinstance(carry, Definition):
                    left_destinations = services.posture_graph_service().all_mobile_nodes_at_none_no_carry
                elif carry.is_in_inventory() or carry.parent not in (None, self.sim):
                    left_destinations = STAND_AT_NONE_NODES
                else:
                    left_destinations = (STAND_AT_NONE_CARRY,)
        self.left_destinations = left_destinations
        paths_right = self.posture_graph._right_path_gen(self.sim, self.interaction, self._distance_estimator, left_destinations, self.destinations, self.var_map, self.constraint, self.valid_edge_test, path_left, allow_carried=allow_carried)
        for path_right in paths_right:
            path_right.segmented_path = self
            yield path_right

    def generate_middle_paths(self, path_left, path_right):
        if self.is_complete:
            yield None
            return
        middle_paths = self.posture_graph._middle_path_gen(path_left, path_right, self.sim, self.interaction, self._distance_estimator, self.var_map)
        for path_middle in middle_paths:
            path_middle.segmented_path = self
            yield path_middle

    @property
    def _path(self):
        return algos.Path(list(getattr(self, '_path_left', ['...?'])) + list(getattr(self, '_path_middle', ['...', '...?']) or [])[1:] + list(getattr(self, '_path_right', ['...', '...?']))[1:])

    def __repr__(self):
        if self.is_complete:
            return 'CompleteSegmentedPath(...)'
        return 'SegmentedPath(...)'

class Connectivity:

    def __init__(self, best_complete_path, source_destination_sets, source_middle_sets, middle_destination_sets):
        self.best_complete_path = best_complete_path
        self.source_destination_sets = source_destination_sets
        self.source_middle_sets = source_middle_sets
        self.middle_destination_sets = middle_destination_sets

    def __repr__(self):
        return 'Connectivity%r' % (tuple(self),)

    def __bool__(self):
        return any(self)

    def __iter__(self):
        return iter((self.best_complete_path, self.source_destination_sets, self.source_middle_sets, self.middle_destination_sets))

    def __getitem__(self, i):
        return (self.best_complete_path, self.source_destination_sets, self.source_middle_sets, self.middle_destination_sets)[i]

class TransitionSequenceStage(enum.Int, export=False):
    EMPTY = ...
    TEMPLATES = ...
    PATHS = ...
    CONNECTIVITY = ...
    ROUTES = ...
    ACTOR_TARGET_SYNC = ...
    COMPLETE = ...

class SequenceId(enum.Int, export=False):
    DEFAULT = 0
    PICKUP = 1
    PUTDOWN = 2
_MobileNode = namedtuple('_MobileNode', ('graph_node', 'prev'))COST_DELIMITER_STR = '----------------------------------'
def _shortest_path_gen(sim, sources, destinations, *args, **kwargs):
    if gsi_handlers.posture_graph_handlers.archiver.enabled:
        gsi_handlers.posture_graph_handlers.log_path_cost(sim, COST_DELIMITER_STR, COST_DELIMITER_STR, (COST_DELIMITER_STR,))
        gsi_handlers.posture_graph_handlers.add_heuristic_fn_score(sim, '', COST_DELIMITER_STR, COST_DELIMITER_STR, '')

    def is_destination(node):
        if isinstance(node, _MobileNode):
            node = node.graph_node
        return node in destinations

    fake_paths = algos.shortest_path_gen(sources, is_destination, *args, **kwargs)
    for fake_path in fake_paths:
        path = algos.Path([node.graph_node if isinstance(node, _MobileNode) else node for node in fake_path], fake_path.cost)
        yield path

def set_transition_failure_reason(sim, reason, target_id=None, transition_controller=None):
    if transition_controller is None:
        transition_controller = sim.transition_controller
    if transition_controller is not None:
        transition_controller.set_failure_target(sim, reason, target_id=target_id)

def _cache_global_sim_default_values():
    global SIM_DEFAULT_POSTURE_TYPE, STAND_AT_NONE, STAND_AT_NONE_CARRY, STAND_AT_NONE_NODES, SIM_DEFAULT_AOPS, SIM_DEFAULT_OPERATION, SIM_SWIM_POSTURE_TYPE, SWIM_AT_NONE, SWIM_AT_NONE_CARRY, SWIM_AT_NONE_NODES, SIM_SWIM_AOPS, SIM_SWIM_OPERATION, _MOBILE_NODES_AT_NONE, _MOBILE_NODES_AT_NONE_CARRY, _DEFAULT_MOBILE_NODES
    SIM_DEFAULT_POSTURE_TYPE = PostureGraphService.get_default_affordance(Species.HUMAN).provided_posture_type
    STAND_AT_NONE = get_origin_spec(SIM_DEFAULT_POSTURE_TYPE)
    STAND_AT_NONE_CARRY = get_origin_spec_carry(SIM_DEFAULT_POSTURE_TYPE)
    STAND_AT_NONE_NODES = (STAND_AT_NONE, STAND_AT_NONE_CARRY)
    SIM_DEFAULT_AOPS = enumdict(Species, {species: AffordanceObjectPair(affordance, None, affordance, None, force_inertial=True) for (species, affordance) in PostureGraphService.SIM_DEFAULT_AFFORDANCES.items()})
    SIM_DEFAULT_OPERATION = PostureOperation.BodyTransition(SIM_DEFAULT_POSTURE_TYPE, SIM_DEFAULT_AOPS)
    SIM_SWIM_POSTURE_TYPE = PostureGraphService.get_default_swim_affordance(Species.HUMAN).provided_posture_type
    SWIM_AT_NONE = get_origin_spec(SIM_SWIM_POSTURE_TYPE)
    SWIM_AT_NONE_CARRY = get_origin_spec_carry(SIM_SWIM_POSTURE_TYPE)
    SWIM_AT_NONE_NODES = (SWIM_AT_NONE, SWIM_AT_NONE_CARRY)
    SIM_SWIM_AOPS = enumdict(Species, {species: AffordanceObjectPair(affordance, None, affordance, None, force_inertial=True) for (species, affordance) in PostureGraphService.SWIM_DEFAULT_AFFORDANCES.items()})
    SIM_SWIM_OPERATION = PostureOperation.BodyTransition(SIM_SWIM_POSTURE_TYPE, SIM_SWIM_AOPS)
    _MOBILE_NODES_AT_NONE = {STAND_AT_NONE}
    _MOBILE_NODES_AT_NONE_CARRY = {STAND_AT_NONE_CARRY}
    _DEFAULT_MOBILE_NODES = {STAND_AT_NONE, STAND_AT_NONE_CARRY}
    for affordance in PostureGraphService.POSTURE_PROVIDING_AFFORDANCES:
        if affordance.provided_posture_type is not None and affordance.provided_posture_type.mobile and not affordance.provided_posture_type.skip_route:
            posture_type = affordance.provided_posture_type
            mobile_node_at_none = get_origin_spec(posture_type)
            _MOBILE_NODES_AT_NONE.add(mobile_node_at_none)
            _DEFAULT_MOBILE_NODES.add(mobile_node_at_none)
            if posture_type._supports_carry:
                mobile_node_at_none_carry = get_origin_spec_carry(posture_type)
                _MOBILE_NODES_AT_NONE_CARRY.add(mobile_node_at_none_carry)
                _DEFAULT_MOBILE_NODES.add(mobile_node_at_none_carry)

def get_mobile_posture_constraint(posture=None, target=None):
    posture_manifests = []
    body_target = target
    if posture is not None:
        if posture is SIM_DEFAULT_POSTURE_TYPE:
            return STAND_AT_NONE_CONSTRAINT
        if posture is SIM_SWIM_POSTURE_TYPE:
            return SWIM_AT_NONE_CONSTRAINT
        if not posture.mobile:
            logger.error('Cannot create mobile posture constraint from non-mobile posture {}', posture)
            return Nowhere('Mobile posture override {} is not actually mobile.', posture)
        else:
            posture_manifests = [posture.get_provided_postures()]
            if posture_manifests or target is not None:
                for mobile_posture in target.provided_mobile_posture_types:
                    posture_manifests.append(mobile_posture.get_provided_postures())
                    body_target = None
                    break
            elif target.routing_component is None:
                body_target = PostureSpecVariable.ANYTHING
            constraints = []
            for manifest in posture_manifests:
                posture_state_spec = create_body_posture_state_spec(manifest, body_target=body_target)
                constraint = Constraint(debug_name='MobilePosture@None', posture_state_spec=posture_state_spec)
                constraints.append(constraint)
            if constraints:
                return create_constraint_set(constraints, debug_name='MobilePostureConstraints')
    if posture_manifests or target is not None:
        for mobile_posture in target.provided_mobile_posture_types:
            posture_manifests.append(mobile_posture.get_provided_postures())
            body_target = None
            break
    elif target.routing_component is None:
        body_target = PostureSpecVariable.ANYTHING
    constraints = []
    for manifest in posture_manifests:
        posture_state_spec = create_body_posture_state_spec(manifest, body_target=body_target)
        constraint = Constraint(debug_name='MobilePosture@None', posture_state_spec=posture_state_spec)
        constraints.append(constraint)
    if constraints:
        return create_constraint_set(constraints, debug_name='MobilePostureConstraints')
    return STAND_AT_NONE_CONSTRAINT

def is_object_mobile_posture_compatible(obj):
    return any(posture_type.posture_objects is not None for posture_type in obj.provided_mobile_posture_types)

@contextmanager
def supress_posture_graph_build(rebuild=True):
    posture_graph_service = services.current_zone().posture_graph_service
    posture_graph_service.disable_graph_building()
    try:
        yield None
    finally:
        posture_graph_service.enable_graph_building()
        if rebuild:
            posture_graph_service.rebuild()

def can_remove_blocking_sims(sim, interaction, required_targets):
    need_to_cancel = []
    blocking_sims = set()
    for obj in required_targets:
        obj_users = obj.get_users()
        if obj.is_part:
            obj = obj.part_owner
            obj_users = obj.get_users()
        for blocking_sim in obj_users:
            if blocking_sim is sim:
                pass
            else:
                if not blocking_sim.is_sim:
                    return (False, need_to_cancel, blocking_sims)
                for blocking_si in blocking_sim.si_state:
                    if not obj.is_same_object_or_part(blocking_si.target):
                        pass
                    else:
                        if blocking_si.can_shoo and blocking_si.priority >= interaction.priority:
                            return (False, need_to_cancel, blocking_sims)
                        need_to_cancel.append(blocking_si)
                        blocking_sims.add(blocking_sim)
    return (True, need_to_cancel, blocking_sims)

class TransitionSpec:
    DISTANCE_TO_FADE_SIM_OUT = Tunable(description='\n        Distance at which a Sim will start fading out if tuned as such.\n        ', tunable_type=float, default=5.0)

@cython.cfunc
@cython.exceptval(check=False)
def TransitionSpecCython_create(path_spec, posture_spec:PostureSpec, var_map, sequence_id=SequenceId.DEFAULT, portal_obj=None, portal_id=None) -> 'TransitionSpecCython':
    self = cython.declare(TransitionSpecCython, TransitionSpecCython.__new__(TransitionSpecCython))
    self.posture_spec = posture_spec
    self._path_spec = path_spec
    self.var_map = var_map
    self.path = None
    self.final_constraint = None
    self._transition_interactions = {}
    self.sequence_id = sequence_id
    self.locked_params = frozendict()
    self._additional_reservation_handlers = []
    self.handle_slot_reservations = False
    self._portal_ref = portal_obj.ref() if portal_obj is not None else None
    self.portal_id = portal_id
    self.created_posture_state = None
    return self
