from server_commands.argument_helpers import TunableInstanceParamimport sims4.commandsimport services
@sims4.commands.Command('calendar.set_favorite_calendar_entry', command_type=sims4.commands.CommandType.Live)
def set_favorite_calendar_entry(event_id:int, is_favorite:bool=False, _connection=None):
    services.calendar_service().set_favorited_calendar_entry(event_id, is_favorite)
