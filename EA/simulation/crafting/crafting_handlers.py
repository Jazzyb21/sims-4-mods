from gsi_handlers.gameplay_archiver import GameplayArchiver
    sub_schema.add_field('visible', label='Visible')
    sub_schema.add_field('progress', label='Current Progress')
    sub_schema.add_field('turns', label='Max Turns')
    sub_schema.add_field('phase_type', label='Phase Type')
    sub_schema.add_field('skill', label='Skill adjustment')
    sub_schema.add_field('ingredient', label='Ingredient adjustment')
    sub_schema.add_field('base', label='Base quality')
    sub_schema.add_field('multiplied', label='Multiplied quality')
    sub_schema.add_field('final', label='Final quality')
    sub_schema.add_field('ingredient', label='Ingredient consumed')
    sub_schema.add_field('quality', label='Ingredient quality')
    sub_schema.add_field('count', label='Ingredient count')
def log_process(process, sim_id, interaction, logger_crafting):
    interaction_name = '{}({})'.format(interaction.affordance.__name__, interaction.id)
    archive_data = {'recipe': process.recipe.__name__, 'affordance': interaction_name, 'phase': str(process.phase), 'crafter': _get_sim_name(process.crafter)}
    archive_data['ingredients'] = []
    archive_data['quality applied'] = []
    archive_data['phase_details'] = logger_crafting
    logger_crafting['visible'] = str(process.phase.is_visible) if process.phase is not None else 'False'
    archiver.archive(data=archive_data, object_id=sim_id)

def log_ingredient_calculation(process, sim_id, ingredient_log):
    archive_data = {'recipe': process.recipe.__name__, 'affordance': 'ingredient consumption', 'phase': 'ingredient consumption', 'crafter': _get_sim_name(process.crafter)}
    archive_data['ingredient consumption'] = ingredient_log
    archiver.archive(data=archive_data, object_id=sim_id)

def log_quality(process, sim_id, quality_entry):
    archive_data = {'recipe': process.recipe.__name__, 'affordance': 'quality applied', 'phase': 'quality applied', 'crafter': _get_sim_name(process.crafter)}
    archive_data['ingredient consumption'] = []
    archive_data['quality applied'] = quality_entry
    archiver.archive(data=archive_data, object_id=sim_id)

def _get_sim_name(sim):
    if sim is not None:
        s = '{}[{}]'.format(sim.full_name, standard_brief_id_repr(sim.id))
        s = _get_csv_friendly_string(s)
        return s
    return ''
