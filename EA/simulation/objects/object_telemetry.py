import sims4import telemetry_helperTELEMETRY_GROUP_OBJECT = 'OBJC'writer = sims4.telemetry.TelemetryWriter(TELEMETRY_GROUP_OBJECT)TELEMETRY_HOOK_STATE_CHANGE = 'OBJC'TELEMETRY_FIELD_DEFINITION = 'objc'TELEMETRY_FIELD_INSTANCE = 'inst'TELEMETRY_FIELD_OLD_STATE = 'from'TELEMETRY_FIELD_NEW_STATE = 'news'TELEMETRY_FIELD_REASON = 'resn'
def send_state_change_telemetry(obj, old_value, new_value, from_init, from_stat, from_sync):
    with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_STATE_CHANGE) as hook:
        definition_id = obj.definition.id if hasattr(obj, 'definition') else 0
        hook.write_int(TELEMETRY_FIELD_DEFINITION, definition_id)
        hook.write_int(TELEMETRY_FIELD_INSTANCE, obj.id)
        hook.write_enum(TELEMETRY_FIELD_OLD_STATE, old_value)
        hook.write_enum(TELEMETRY_FIELD_NEW_STATE, new_value)
        if from_init:
            reason = 'init'
        elif from_stat:
            reason = 'stat'
        elif from_sync:
            reason = 'sync'
        else:
            reason = 'other'
        hook.write_string(TELEMETRY_FIELD_REASON, reason)
TELEMETRY_HOOK_OBJECT_CREATE_BSCEXTRA = 'CRBE'TELEMETRY_FIELD_OBJECT_INTERACTION = 'intr'TELEMETRY_FIELD_OBJECT_DEFINITION = 'objc'
def send_create_object_basic_extra_telemetry(interaction_id, definition_id):
    with telemetry_helper.begin_hook(writer, TELEMETRY_HOOK_OBJECT_CREATE_BSCEXTRA) as hook:
        hook.write_int(TELEMETRY_FIELD_OBJECT_INTERACTION, interaction_id)
        hook.write_guid(TELEMETRY_FIELD_OBJECT_DEFINITION, definition_id)
