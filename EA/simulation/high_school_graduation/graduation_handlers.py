import services
@GsiHandler('graduation_service', graduate_service_schema)
def generate_graduation_service_view_data(sim_id:int=None):
    grad_service = services.get_graduation_service()
    if grad_service is None:
        return []
    all_grads = []
    for sim_info in grad_service.graduating_sims_gen():
        graduate_data = {}
        graduate_data['sim_id'] = sim_info.id
        graduate_data['sim_first_name'] = sim_info.first_name
        graduate_data['sim_last_name'] = sim_info.last_name
        graduate_data['current_graduation'] = grad_service.is_sim_info_graduating(sim_info)
        graduate_data['valedictorian'] = grad_service.is_current_valedictorian(sim_info)
        graduate_data['waiting_valedictorian'] = grad_service.is_waiting_valedictorian(sim_info)
        all_grads.append(graduate_data)
    return all_grads
