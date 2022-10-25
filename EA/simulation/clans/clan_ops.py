from protocolbuffers import DistributorOps_pb2from distributor.ops import Opfrom distributor.rollback import ProtocolBufferRollback
class ClanMembershipUpdateOp(Op):

    def __init__(self, update_type, clan_id):
        super().__init__()
        self.op = DistributorOps_pb2.ClanMembershipUpdate()
        self.op.clan_id = clan_id
        self.op.update_type = update_type

    def write(self, msg):
        self.serialize_op(msg, self.op, DistributorOps_pb2.Operation.CLAN_MEMBERSHIP_UPDATE)

class ClanUpdateOp(Op):

    def __init__(self, clan_guid_to_leader_id_map, clan_alliance_status):
        super().__init__()
        self.op = DistributorOps_pb2.ClanUpdate()
        for (clan_guid, leader_id) in clan_guid_to_leader_id_map.items():
            with ProtocolBufferRollback(self.op.clan_leaders) as clan_leaders_msg:
                clan_leaders_msg.clan_guid = clan_guid
                clan_leaders_msg.leader_sim_id = leader_id
        if clan_alliance_status is not None:
            self.op.clan_alliance_state = clan_alliance_status

    def write(self, msg):
        self.serialize_op(msg, self.op, DistributorOps_pb2.Operation.CLAN_UPDATE)
