import sims4.logimport telemetry_helperfrom sims4.telemetry import TelemetryWriterTELEMETRY_GROUP_BUILD_BUY = 'BDBY'TELEMETRY_HOOK_OPENABLE_WINDOW = 'WOPN'TELEMETRY_OBJECT_DEF_ID = 'owid'TELEMETRY_OPENABLE_WINDOW_COUNT = 'nmow'buildbuy_telemetry_writer = TelemetryWriter(TELEMETRY_GROUP_BUILD_BUY)logger = sims4.log.Logger('PortalTelemetry', default_owner='yecao')
def write_portal_telemetry(hook_tag, obj_def_id, routable_window_count):
    logger.debug('{}: {}: {} successfully generated portal', hook_tag, obj_def_id, routable_window_count)
    with telemetry_helper.begin_hook(buildbuy_telemetry_writer, hook_tag) as hook:
        hook.write_int(TELEMETRY_OBJECT_DEF_ID, obj_def_id)
        hook.write_int(TELEMETRY_OPENABLE_WINDOW_COUNT, routable_window_count)
