import services
    sub_schema.add_field('cost', label='Cost')
    sub_schema.add_field('enabled', label='Enabled')
    sub_schema.add_field('footprint_id', label='Footprint Id')
    sub_schema.add_field('footprint_type', label='Footprint Type')
    sub_schema.add_field('polygon', label='Polygon')
    sub_schema.add_field('embarrassed_affordance', label='Embarrassed Affordance')
    sub_schema.add_field('post_route_affordance', label='Post Route Affordance')
    sub_schema.add_field('allowed_sims', label='Allowed Sims')
    sub_schema.add_field('disallowed_sims', label='Disallowed Sims')
    sub_schema.add_field('exempt_sims', label='Sims Exempt From Shooing')
    privacy_instance_to_violators = weakref.WeakKeyDictionary()
@GsiHandler('privacy_management', privacy_management_schema)
def generate_privacy_management_data(filter=None):
    privacy_management_data = []
    active_instances = []
    filter_list = parse_filter_to_list(filter)
    privacy_service = services.privacy_service()
    if privacy_service is None:
        return privacy_management_data
    for instance in privacy_service._privacy_instances:
        if instance.is_active:
            active_instances.append(instance)
        if (filter_list is None or ACTIVE_FILTER not in filter_list) and instance.is_active:
            pass
        elif filter_list is not None and HAS_VIOLATORS_FILTER in filter_list and not (instance.find_violating_vehicles() or instance.find_violating_sims() or instance._late_violators):
            pass
        else:
            entry = {'is_active': str(instance.is_active), 'max_los': str(instance._max_line_of_sight_radius), 'has_shooed': str(instance.has_shooed), 'privacy_violators': str(instance.privacy_violators), 'privacy_discouragement_cost': str(instance.privacy_discouragement_cost), 'privacy_interaction': str(instance._interaction), 'central_object': str(instance.central_object), 'shoo_cons': str(instance._shoo_constraint_radius or instance._SHOO_CONSTRAINT_RADIUS), 'affordances': {'embarrassed_affordance': str(instance._embarrassed_affordance or instance._EMBARRASSED_AFFORDANCE), 'post_route_affordance': str(instance._post_route_affordance)}, 'allowed': {'allowed_sims': gsi_handlers.gsi_utils.format_object_list_names(instance._allowed_sims) if instance._allowed_sims else 'None', 'disallowed_sims': gsi_handlers.gsi_utils.format_object_list_names(instance._disallowed_sims) if instance._disallowed_sims else 'None', 'exempt_sims': gsi_handlers.gsi_utils.format_object_list_names(instance._exempt_sims) if instance._exempt_sims else 'None'}, 'privacy_constraints': []}
            populate_violators(entry, instance, active_instances)
            for constraint in instance._privacy_constraints:
                constraint_type = next(constraint_type for (constraint_type, value) in vars(FootprintType).items() if value == constraint.footprint_type)
                entry['privacy_constraints'].append({'cost': str(constraint.cost), 'enabled': str(constraint.enabled), 'footprint_id': str(constraint.footprint_id), 'footprint_type': str(constraint_type), 'polygon': str(constraint.polygon)})
            privacy_management_data.append(entry)
    return privacy_management_data

def populate_violators(entry, instance, active_instances):
    global privacy_instance_to_violators
    entry['sim_violators'] = gsi_handlers.gsi_utils.format_object_list_names(instance.find_violating_sims()) if instance.find_violating_sims() else NO_VIOLATORS_STR
    entry['late_violators'] = gsi_handlers.gsi_utils.format_object_list_names(instance._late_violators) if instance._late_violators else NO_VIOLATORS_STR
    entry['vehicle_violators'] = gsi_handlers.gsi_utils.format_object_list_names(instance.find_violating_vehicles()) if instance.find_violating_vehicles() else NO_VIOLATORS_STR
    for violator in itertools.chain(instance.find_violating_sims(), instance.find_violating_vehicles(), instance._late_violators):
        if privacy_instance_to_violators and instance in privacy_instance_to_violators:
            if str(violator) not in privacy_instance_to_violators[instance]:
                privacy_instance_to_violators[instance].append(str(violator))
                privacy_instance_to_violators.update({instance: [str(violator)]})
        else:
            privacy_instance_to_violators.update({instance: [str(violator)]})
    for (key, value) in privacy_instance_to_violators.items():
        if key is instance:
            entry['all_past_violators'] = [str(violator) for violator in value]
            break
    entry['all_past_violators'] = NO_VIOLATORS_STR
    privacy_instance_to_violators = {instance: violators for (instance, violators) in privacy_instance_to_violators.items() if instance in active_instances}
