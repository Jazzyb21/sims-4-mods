from conditional_layers.conditional_layer_enums import ConditionalLayerRequestSpeedTypefrom server_commands.argument_helpers import TunableInstanceParamimport servicesimport sims4.commands
@sims4.commands.Command('layers.load_layer')
def load_conditional_layer(conditional_layer:TunableInstanceParam(sims4.resources.Types.CONDITIONAL_LAYER), immediate:bool=True, timer_interval:int=1, timer_object_count:int=5):
    if conditional_layer is None:
        sims4.commands.output('Unable to find the conditional_layer instance specified.')
        return
    conditional_layer_service = services.conditional_layer_service()
    speed = ConditionalLayerRequestSpeedType.IMMEDIATELY if immediate else ConditionalLayerRequestSpeedType.GRADUALLY
    conditional_layer_service.load_conditional_layer(conditional_layer, speed=speed, timer_interval=timer_interval, timer_object_count=timer_object_count)

@sims4.commands.Command('layers.destroy_layer')
def destroy_conditional_layer(conditional_layer:TunableInstanceParam(sims4.resources.Types.CONDITIONAL_LAYER), immediate:bool=True, timer_interval:int=1, timer_object_count:int=5):
    conditional_layer_service = services.conditional_layer_service()
    speed = ConditionalLayerRequestSpeedType.IMMEDIATELY if immediate else ConditionalLayerRequestSpeedType.GRADUALLY
    conditional_layer_service.destroy_conditional_layer(conditional_layer, speed=speed, timer_interval=timer_interval, timer_object_count=timer_object_count)

@sims4.commands.Command('layers.reload_layer')
def reload_conditional_layer(conditional_layer:TunableInstanceParam(sims4.resources.Types.CONDITIONAL_LAYER), immediate:bool=True, timer_interval:int=1, timer_object_count:int=5):
    conditional_layer_service = services.conditional_layer_service()
    speed = ConditionalLayerRequestSpeedType.IMMEDIATELY if immediate else ConditionalLayerRequestSpeedType.GRADUALLY
    conditional_layer_service.destroy_conditional_layer(conditional_layer, speed=speed, timer_interval=timer_interval, timer_object_count=timer_object_count)
    conditional_layer_service.load_conditional_layer(conditional_layer, speed=speed, timer_interval=timer_interval, timer_object_count=timer_object_count)

@sims4.commands.Command('layers.active_layers')
def list_active_layers(_connection=None):
    conditional_layer_service = services.conditional_layer_service()
    for (conditional_layer, layer_info) in conditional_layer_service._layer_infos.items():
        if layer_info.last_request_type != ConditionalLayerRequestType.LOAD_LAYER:
            pass
        else:
            msg = '{} : {}'.format(conditional_layer.__name__, len(layer_info.objects_loaded))
            sims4.commands.automation_output(msg, _connection)
            sims4.commands.cheat_output(msg, _connection)
    sims4.commands.automation_output('END', _connection)
