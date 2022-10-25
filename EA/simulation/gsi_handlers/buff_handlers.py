from gsi_handlers.gameplay_archiver import GameplayArchiver
def archive_buff_message(buff_msg, shows_timeout, change_rate):
    buff_reason = hex(buff_msg.reason.hash) if buff_msg.HasField('reason') else None
    entry = {'buff_id': buff_msg.buff_id, 'update_type': str(BuffUpdateType(buff_msg.update_type)), 'buff_reason': buff_reason, 'is_mood_buff': buff_msg.is_mood_buff, 'commodity_guid': buff_msg.commodity_guid, 'transition_into_buff_id': buff_msg.transition_into_buff_id}
    manager = services.get_instance_manager(sims4.resources.Types.BUFF)
    if manager:
        buff_cls = manager.get(buff_msg.buff_id)
        entry['buff_name'] = buff_cls.__name__
    if buff_msg.timeout:
        entry['timeout'] = buff_msg.timeout
        entry['rate'] = buff_msg.rate_multiplier
    if change_rate is not None:
        if buff_msg.buff_progress == Sims_pb2.BUFF_PROGRESS_NONE:
            entry['progress_arrow'] = 'No Arrow'
        elif buff_msg.buff_progress == Sims_pb2.BUFF_PROGRESS_UP:
            entry['progress_arrow'] = 'Arrow Up'
        else:
            entry['progress_arrow'] = 'Arrow Down'
    if buff_msg.update_type != BuffUpdateType.REMOVE and shows_timeout and buff_msg.HasField('mood_type_override'):
        entry['mood_type_override'] = buff_msg.mood_type_override
    sim_buff_log_archiver.archive(data=entry, object_id=buff_msg.sim_id)

    sub_schema.add_field('buff_id', label='Buff ID')
    sub_schema.add_field('buff_name', label='Buff name')
    sub_schema.add_field('buff_mood', label='Buff Mood')
    sub_schema.add_field('buff_mood_override', label='Mood Override (current)')
    sub_schema.add_field('buff_mood_override_pending', label='Mood Override (pending)')
def archive_mood_message(sim_id, active_mood, active_mood_intensity, active_buffs, changeable_buffs):
    mood_entry = {'mood_id': active_mood.guid64, 'mood_name': active_mood.__name__, 'mood_intensity': active_mood_intensity}
    active_buff_entries = []
    for (buff_type, buff) in active_buffs.items():
        buff_entry = {'buff_id': buff_type.guid64, 'buff_name': buff_type.__name__, 'buff_mood': buff.mood_type.__name__ if buff.mood_type is not None else 'None', 'buff_mood_override': buff.mood_override.__name__ if buff.mood_override is not None else 'None'}
        for (changeable_buff, new_mood_override) in changeable_buffs:
            if changeable_buff is buff:
                buff_entry['buff_mood_override_pending'] = 'None' if new_mood_override is None else new_mood_override.__name__
                break
        active_buff_entries.append(buff_entry)
    mood_entry['active_buffs'] = active_buff_entries
    sim_mood_log_archiver.archive(data=mood_entry, object_id=sim_id)
