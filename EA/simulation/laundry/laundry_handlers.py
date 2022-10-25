from laundry.laundry_tuning import LaundryTuning
@GsiHandler('laundry', laundry_schema)
def generate_laundry_view():

    def _add_entry(idx, entry, data_list):
        if idx < len(data_list):
            data_list[idx].update(entry)
        else:
            data_list.append(entry)

    laundry_data = []
    laundry_service = services.get_laundry_service()
    condition_timeout = LaundryTuning.PUT_AWAY_FINISHED_LAUNDRY.laundry_condition_timeout
    if laundry_service is not None:
        household = laundry_service.affected_household
        if household is None:
            entry = {'household': str(household)}
            laundry_data.append(entry)
        else:
            now = services.time_service().sim_now
            entry = {'household_id': household.id, 'household': household.name, 'last_unload': str(household.laundry_tracker.last_unload_laundry_time)}
            laundry_data.append(entry)
            for (i, condition) in enumerate(household.laundry_tracker.finished_laundry_conditions.values()):
                time_remaining = condition_timeout - (now - condition[0]).in_minutes()
                entry = {'conditions': str(condition[1]), 'remaining': str(time_remaining) if time_remaining > 0 else 'EXPIRED'}
                _add_entry(i, entry, laundry_data)
            for (i, hero_obj) in enumerate(laundry_service.laundry_hero_objects):
                entry = {'hero_objects_id': hex(hero_obj.id), 'hero_objects': hero_obj.definition.name}
                _add_entry(i, entry, laundry_data)
            state_type = LaundryTuning.PUT_CLOTHING_PILE_ON_HAMPER.full_hamper_state.state
            for (i, hamper) in enumerate(laundry_service.hampers):
                entry = {'hampers_id': hex(hamper.id), 'hampers': hamper.definition.name, 'hampers_state': str(hamper.get_state(state_type))}
                _add_entry(i, entry, laundry_data)
    return laundry_data
