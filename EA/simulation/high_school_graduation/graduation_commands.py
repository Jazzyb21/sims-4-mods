import servicesimport sims4from server_commands.argument_helpers import OptionalTargetParam, get_optional_target
@sims4.commands.Command('graduation.set_current_graduate')
def set_current_graduate(opt_sim:OptionalTargetParam=None, _connection=None):
    graduation_service = services.get_graduation_service()
    if graduation_service is None:
        sims4.commands.output("Can't run graduation cheats without EP12 installed")
        return
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        return
    sim_info = sim.sim_info
    if graduation_service.is_sim_info_graduating(sim_info):
        return
    graduation_service.remove_sim_info_waiting_to_graduate(sim_info)
    graduation_service.add_sim_info_as_current_graduate(sim_info)

@sims4.commands.Command('graduation.set_waiting_graduate')
def set_waiting_graduate(opt_sim:OptionalTargetParam=None, _connection=None):
    graduation_service = services.get_graduation_service()
    if graduation_service is None:
        sims4.commands.output("Can't run graduation cheats without EP12 installed")
        return
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        return
    sim_info = sim.sim_info
    if graduation_service.is_sim_info_waiting_to_graduate(sim_info):
        return
    graduation_service.remove_sim_info_currently_graduating(sim_info)
    graduation_service.add_sim_info_as_waiting_graduate(sim_info)

@sims4.commands.Command('graduation.set_current_valedictorian')
def set_current_valedictorian(opt_sim:OptionalTargetParam=None, _connection=None):
    graduation_service = services.get_graduation_service()
    if graduation_service is None:
        sims4.commands.output("Can't run graduation cheats without EP12 installed")
        return
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        return
    sim_info = sim.sim_info
    if graduation_service.is_waiting_valedictorian(sim_info):
        graduation_service.clear_waiting_valedictorian()
    graduation_service.set_current_valedictorian(sim_info)

@sims4.commands.Command('graduation.set_waiting_valedictorian')
def set_waiting_valedictorian(opt_sim:OptionalTargetParam=None, _connection=None):
    graduation_service = services.get_graduation_service()
    if graduation_service is None:
        sims4.commands.output("Can't run graduation cheats without EP12 installed")
        return
    sim = get_optional_target(opt_sim, _connection)
    if sim is None:
        return
    sim_info = sim.sim_info
    if graduation_service.is_current_valedictorian(sim_info):
        graduation_service.clear_current_valedictorian()
    graduation_service.set_waiting_valedictorian(sim_info)
