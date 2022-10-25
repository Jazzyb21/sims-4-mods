import sims4.log
def write_portal_telemetry(hook_tag, obj_def_id, routable_window_count):
    logger.debug('{}: {}: {} successfully generated portal', hook_tag, obj_def_id, routable_window_count)
    with telemetry_helper.begin_hook(buildbuy_telemetry_writer, hook_tag) as hook:
        hook.write_int(TELEMETRY_OBJECT_DEF_ID, obj_def_id)
        hook.write_int(TELEMETRY_OPENABLE_WINDOW_COUNT, routable_window_count)
