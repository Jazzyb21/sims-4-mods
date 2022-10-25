from protocolbuffers import Routing_pb2
class FormationTypePaired(FormationTypeBase):

    @classproperty
    def routing_type():
        return FormationRoutingType.PARIED

    @property
    def slave_attachment_type(self):
        return Routing_pb2.SlaveData.SLAVE_PAIRED_CHILD
