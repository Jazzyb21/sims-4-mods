import sims4.commandsfrom sims4.common import Packimport services
@sims4.commands.Command('fashion_trends.refresh_thrift_store_inventory', pack=Pack.EP12, command_type=sims4.commands.CommandType.DebugOnly)
def fashion_trends_refresh_thrift_store(_connection=None):
    fashion_trend_service = services.fashion_trend_service()
    if fashion_trend_service is None:
        sims4.commands.automation_output('Pack not loaded', _connection)
        sims4.commands.cheat_output('Pack not loaded', _connection)
        return
    fashion_trend_service.debug_randomize_thrift_store_inventory()
