import sims4.commands
from protocolbuffers import Consts_pb2
import services


@sims4.commands.Command('motherlode_plus', command_type=sims4.commands.CommandType.Live,
                        console_type=sims4.commands.CommandType.Cheat)
def motherlode_plus(amount: int = 0, _connection=None):
    tgt_client = services.client_manager().get(_connection)
    modify_fund_helper(amount, Consts_pb2.TELEMETRY_MONEY_CHEAT, tgt_client.active_sim)


def modify_fund_helper(amount, reason, sim):
    if amount > 0:
        sim.family_funds.add(amount, reason, sim)
    else:
        sim.family_funds.try_remove(-amount, reason, sim)
