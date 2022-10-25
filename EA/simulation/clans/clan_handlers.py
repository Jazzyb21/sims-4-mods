import services
    remove_leader_command.add_token_param('clan_id')
    make_new_leader_command.add_token_param('clan_id')
@GsiHandler('clans', clan_schema)
def generate_clans_view():
    clans = []
    clan_service = services.clan_service()
    if clan_service is not None:
        for clan_tuning_data in ClanService.CLAN_DATA:
            clan_guid = clan_tuning_data.guid64
            leader_sim_id = clan_service.clan_guid_to_leader_sim_id_map.get(clan_guid)
            leader_sim_name = ''
            if leader_sim_id is not None:
                leader_sim_info = services.sim_info_manager().get(leader_sim_id)
                leader_sim_name = leader_sim_info.full_name if leader_sim_info is not None else '<missing sim info>'
            clan_data = {'clan_id': str(clan_guid), 'clan_name': str(clan_tuning_data), 'leader_id': str(leader_sim_id), 'leader_name': leader_sim_name, 'alliance_state': str(clan_service.current_clan_alliance_state)}
            clans.append(clan_data)
    return clans
