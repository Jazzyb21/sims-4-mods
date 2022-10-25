import servicesfrom server_commands.argument_helpers import TunableInstanceParamfrom sims4.commands import CommandTypeimport sims4
@sims4.commands.Command('clans.show_clan_information', command_type=sims4.commands.CommandType.Live)
def show_clan_information(clan:TunableInstanceParam(sims4.resources.Types.CLAN), _connection=None):
    clan_service = services.clan_service()
    if clan_service is None:
        return
    clan_service.show_clan_information(clan, services.active_sim_info())

@sims4.commands.Command('clans.remove_clan_leader', command_type=sims4.commands.CommandType.DebugOnly)
def remove_clan_leader(clan:TunableInstanceParam(sims4.resources.Types.CLAN), _connection=None):
    clan_service = services.clan_service()
    if clan_service is None:
        return
    clan_service.remove_clan_leader(clan)

@sims4.commands.Command('clans.replace_clan_leader', command_type=sims4.commands.CommandType.DebugOnly)
def replace_clan_leader(clan:TunableInstanceParam(sims4.resources.Types.CLAN), _connection=None):
    clan_service = services.clan_service()
    if clan_service is None:
        return
    clan_service.remove_clan_leader(clan)
    clan_service.create_clan_leader(clan)
