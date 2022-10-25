import servicesimport sims4from sims4.common import Pack
@sims4.commands.Command('body_type_level.set_acne_enabled', pack=Pack.EP12, command_type=sims4.commands.CommandType.Live)
def set_acne_enabled(enabled:bool=True, _connection=None):
    services.sim_info_manager().set_acne_enabled(enabled)
    return True
