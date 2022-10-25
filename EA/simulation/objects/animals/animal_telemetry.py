import sims4
def send_animal_added_telemetry(animal):
    with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_ADD_ANIMAL) as hook:
        definition_id = animal.definition.id if hasattr(animal, 'definition') else 0
        hook.write_int(TELEMETRY_FIELD_DEFINITION, definition_id)
        hook.write_int(TELEMETRY_FIELD_INSTANCE, animal.id)
