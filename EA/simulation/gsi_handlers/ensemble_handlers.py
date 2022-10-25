from sims4.gsi.dispatcher import GsiHandler
    sub_schema.add_field('sim_name', label='Sim')
    sub_schema.add_field('floor', label='Floor')
@GsiHandler('ensemble_service', ensemble_service_schema)
def generate_drama_scheduler_data(zone_id:int=None):
    all_ensembles = []
    ensemble_service = services.ensemble_service()
    if ensemble_service is None:
        return all_ensembles
    for ensemble in ensemble_service.get_all_ensembles():
        sim_data = []
        for sim in ensemble._sims:
            sim_data.append({'sim_name': sim.full_name, 'floor': sim.level})
        all_ensembles.append({'ensemble_type': str(ensemble), 'number_of_sims': len(ensemble._sims), 'last_floor': ensemble.last_selected_level if ensemble.last_selected_level is not None else 0, 'last_center_of_mass': str(ensemble.last_center_of_mass) if ensemble.last_center_of_mass is not None else 0, 'Sims': sim_data})
    return all_ensembles
