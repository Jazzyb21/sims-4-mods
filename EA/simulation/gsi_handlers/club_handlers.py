from clubs.club_enums import ClubHangoutSetting
def generate_all_club_seeds():
    instance_manager = services.get_instance_manager(sims4.resources.Types.CLUB_SEED)
    if instance_manager.all_instances_loaded:
        return [cls.__name__ for cls in instance_manager.types.values()]
    return []

def add_club(manager):
    with club_schema.add_view_cheat('clubs.create_club_from_seed', label='Create Club') as cheat:
        cheat.add_token_param('club_seed', dynamic_token_fn=generate_all_club_seeds)

    cheat.add_token_param('club_id')
    cheat.add_token_param('sim_id')
    cheat.add_token_param('club_id')
    cheat.add_token_param('club_id')
    cheat.add_token_param('club_id')
    cheat.add_token_param('club_id')
def get_buck_amounts():
    return (1, 10, 100, 1000)

    cheat.add_static_param('ClubBucks')
    cheat.add_token_param('amount', dynamic_token_fn=get_buck_amounts)
    cheat.add_token_param('club_id')
    sub_schema.add_field('sim_id', label='Sim ID', width=0.35)
    sub_schema.add_field('sim_name', label='Sim Name', width=0.4)
    sub_schema.add_field('is_leader', label='Is Leader')
    sub_schema.add_field('sim_id', label='Sim ID', width=0.35)
    sub_schema.add_field('sim_name', label='Sim Name', width=0.4)
    sub_schema.add_field('rule', label='Rule')
    sub_schema.add_field('criteria', label='Criteria')
@GsiHandler('club_info', club_schema)
def generate_club_info_data():
    club_service = services.get_club_service()
    if club_service is None:
        return
    sim_info_manager = services.sim_info_manager()
    club_info = []
    for club in club_service.clubs:
        if club.hangout_setting == ClubHangoutSetting.HANGOUT_VENUE:
            club_hangout_str = 'Venue: {}'.format(str(club.hangout_venue))
        elif club.hangout_setting == ClubHangoutSetting.HANGOUT_LOT:
            club_hangout_str = 'Zone: {}'.format(club.hangout_zone_id)
        else:
            club_hangout_str = 'None'
        entry = {'name': str(club), 'club_id': str(club.club_id), 'hangout': club_hangout_str, 'associated_color': str(club.associated_color) if club.associated_color else 'None', 'uniform_male_child': str(bool(club.uniform_male_child)), 'uniform_female_child': str(bool(club.uniform_female_child)), 'uniform_male_adult': str(bool(club.uniform_male_adult)), 'uniform_female_adult': str(bool(club.uniform_female_adult))}
        members_info = []
        entry['club_members'] = members_info
        for sim in club.members:
            group_members_entry = {'sim_id': str(sim.id), 'sim_name': sim.full_name, 'is_leader': str(sim is club.leader)}
            members_info.append(group_members_entry)
        entry['club_recent_members'] = [{'sim_id': str(sim_id), 'sim_name': str(sim_info_manager.get(sim_id))} for sim_id in club._recent_member_ids]
        rules_info = []
        entry['club_rules'] = rules_info
        if club.rules:
            for rule in club.rules:
                rules_entry = {'rule': str(rule)}
                rules_info.append(rules_entry)
        criteria_info = []
        entry['membership_criteria'] = criteria_info
        if club.membership_criteria:
            for criteria in club.membership_criteria:
                criteria_entry = {'criteria': str(criteria)}
                criteria_info.append(criteria_entry)
        club_info.append(entry)
    return club_info
