from google.protobuf import descriptor
class DebugViz_LineSet(message.Message, metaclass=reflection.GeneratedProtocolMessageType):

    class Line(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
        DESCRIPTOR = _DEBUGVIZ_LINESET_LINE

    DESCRIPTOR = _DEBUGVIZ_LINESET

class DebugViz_Text(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DEBUGVIZ_TEXT

class DebugViz_Layer(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DEBUGVIZ_LAYER

class DebugViz_LayerUpdateNotification(message.Message, metaclass=reflection.GeneratedProtocolMessageType):
    DESCRIPTOR = _DEBUGVIZ_LAYERUPDATENOTIFICATION
