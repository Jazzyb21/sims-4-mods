import servicesimport sims4.commandsfrom global_flags.global_flags import GlobalFlags
@sims4.commands.Command('flags.add_flag', command_type=sims4.commands.CommandType.Automation)
def add_flag(flag:GlobalFlags, connection=None):
    services.global_flag_service().add_flag(flag)

@sims4.commands.Command('flags.remove_flag', command_type=sims4.commands.CommandType.Automation)
def remove_flag(flag:GlobalFlags, connection=None):
    services.global_flag_service().remove_flag(flag)
