import services
def on_sim_killed_or_culled(sim_info):
    clan_service = services.clan_service()
    if clan_service is not None:
        clan_service.on_sim_killed_or_culled(sim_info)
