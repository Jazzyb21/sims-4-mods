from gsi_handlers.gameplay_archiver import GameplayArchiver
    sub_schema.add_field('test_result', label='Test Result', width=2)
    sub_schema.add_field('balloon_type', label='Type', width=2)
    sub_schema.add_field('icon', label='Icon', width=2)
    sub_schema.add_field('weight', label='Weight', type=GsiFieldVisualizers.INT, width=1)
    sub_schema.add_field('balloon_category', label='Category', width=2)
def archive_balloon_data(balloon_object, interaction, result, icon, entries):
    if not balloon_object.is_sim:
        return
    if result is not None:
        weight = result.weight
        balloon_type = str(result.balloon_type)
        gsi_category = result.gsi_category
    else:
        weight = 0
        balloon_type = 'None'
        gsi_category = 'None'
    entry = {}
    entry['sim'] = str(balloon_object)
    entry['interaction'] = str(interaction)
    entry['weight'] = weight
    entry['balloon_type'] = balloon_type
    entry['icon'] = str(icon)
    entry['balloon_category'] = gsi_category
    entry['total_weight'] = sum(entry['weight'] for entry in entries)
    entry['Considered'] = entries
    archiver.archive(data=entry, object_id=balloon_object.id)
