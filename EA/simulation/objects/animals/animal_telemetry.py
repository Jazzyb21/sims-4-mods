import sims4import telemetry_helperTELEMETRY_GROUP_ANIMAL = 'ANML'writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_ANIMAL)TELEMETRY_HOOK_ADD_ANIMAL = 'AADD'TELEMETRY_FIELD_DEFINITION = 'type'TELEMETRY_FIELD_INSTANCE = 'anid'
def send_animal_added_telemetry(animal):
    with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_ADD_ANIMAL) as hook:
        definition_id = animal.definition.id if hasattr(animal, 'definition') else 0
        hook.write_int(TELEMETRY_FIELD_DEFINITION, definition_id)
        hook.write_int(TELEMETRY_FIELD_INSTANCE, animal.id)
