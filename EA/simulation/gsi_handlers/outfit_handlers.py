from gsi_handlers.gameplay_archiver import GameplayArchiverfrom sims4.gsi.schema import GsiGridSchemafrom sims.outfits.outfit_enums import OutfitCategoryoutfit_log_schema = GsiGridSchema(label='Outfit Archive', sim_specific=True)outfit_log_schema.add_field('type', label='Type')outfit_log_schema.add_field('current_outfit', label='Curent Outfit (Category, Index)')outfit_log_schema.add_field('change_to', label='Change To')outfit_log_schema.add_field('reason', label='Reason')with outfit_log_schema.add_has_many('generated_outfit_data', GsiGridSchema, label='Generated Outfit Data') as sub_schema:
    sub_schema.add_field('name', label='Name')
    sub_schema.add_field('data', label='Data')archiver = GameplayArchiver('outfit_log', outfit_log_schema, add_to_archive_enable_functions=True)
def log_outfit_change(sim_info, change_to, change_reason):
    if sim_info is None or change_to is None:
        return
    entry = {'type': 'change', 'current_outfit': repr((OutfitCategory(sim_info._current_outfit[0]), sim_info._current_outfit[1])), 'change_to': repr((OutfitCategory(change_to[0]), change_to[1])), 'reason': repr(change_reason)}
    archiver.archive(data=entry, object_id=sim_info.id)

def log_outfit_generate(sim_info, outfit_category, outfit_index, tag_list, filter_flag, body_type_chance_overrides, body_type_match_not_found_policy):
    if sim_info is None:
        return
    entry = {'type': 'generate', 'current_outfit': repr((OutfitCategory(outfit_category), outfit_index))}
    generated_outfit_data = []
    generated_outfit_data.append({'name': 'tag_list', 'data': repr(tag_list)})
    generated_outfit_data.append({'name': 'filter_flag', 'data': repr(filter_flag)})
    generated_outfit_data.append({'name': 'body_type_chance_overrides', 'data': repr(body_type_chance_overrides)})
    generated_outfit_data.append({'name': 'body_type_match_not_found_policy', 'data': repr(body_type_match_not_found_policy)})
    entry['generated_outfit_data'] = generated_outfit_data
    archiver.archive(data=entry, object_id=sim_info.id)
