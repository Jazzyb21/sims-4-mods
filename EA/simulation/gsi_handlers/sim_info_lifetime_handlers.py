from gsi_handlers.gameplay_archiver import GameplayArchiver
    sub_schema.add_field('creation_source', label='Creation Source')
    sub_schema.add_field('count', label='Count', type=GsiFieldVisualizers.INT)
def is_archive_enabled():
    return archiver.enabled

def archive_sim_info_event(sim_info, event_type):
    sim_info_manager = services.sim_info_manager()
    if sim_info_manager is None:
        return
    if sim_info is None:
        return
    household = sim_info.household
    household_id = household.id if household is not None else 0
    total_sim_info_count = len(sim_info_manager.values())
    entry = {'game_time': str(services.time_service().sim_now), 'total_sim_info_count': str(total_sim_info_count), 'event_type': event_type, 'sim_id': str(sim_info.id), 'sim_name': sim_info.full_name, 'creation_source': format_enum_name(sim_info.creation_source), 'situations': sim_info.debug_get_current_situations_string(), 'household_id': str(household_id), 'household_name': str(household.name) if household is not None else 'NO HOUSEHOLD'}
    creation_source_info = []
    entry['creation_sources'] = creation_source_info
    creation_sources_and_counts = get_sim_info_creation_sources()
    for (source, count) in creation_sources_and_counts.items():
        creation_source_entry = {'creation_source': source, 'count': str(count)}
        creation_source_info.append(creation_source_entry)
    archiver.archive(entry)
