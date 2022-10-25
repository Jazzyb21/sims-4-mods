from distributor.rollback import ProtocolBufferRollback
class AnimalTypeBase(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'move_to_spawn_point_state_value': ObjectStateValue.TunableReference(description='\n            State value to move the animal to the spawn point. Primary use \n            case is to get the animal out of the way when they are homeless\n            and invisible.\n            '), 'move_to_spawn_point_tags': OptionalTunable(description='\n            Spawn point tags to determine which spawn points to move the animal to. \n            ', tunable=TunableTags(filter_prefixes=('Spawn',)))}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classproperty
    def creature_type(cls):
        raise NotImplementedError

    def setup(self, owner):
        pass

class RabbitAnimalType(AnimalTypeBase):

    @classproperty
    def creature_type(cls):
        return CreatureType.Rabbit

class ChickenAnimalType(AnimalTypeBase):
    FACTORY_TUNABLES = {'terrain_control': TunableTuple(description='\n            Procedural control to send to client to allow chickens to align with terrain.\n            ', control_id=TunableStringHash32(description='\n                The control id. This string will be converted to a hash number and sent to client.\n                '), control=ProceduralControlSkate.TunableFactory(description='\n                Chickens will skate along terrain on defined platform.\n                ', locked_args={'terrain_alignment': True}))}

    def setup(self, owner):
        animation_data_msg = Animation_pb2.ProceduralAnimationData()
        terrain_ctrl = self.terrain_control
        with ProtocolBufferRollback(animation_data_msg.controls) as control_msg:
            control_msg.control_id = terrain_ctrl.control_id
            skate = terrain_ctrl.control()
            skate.build_control_msg(control_msg)
        distributor = Distributor.instance()
        op = GenericProtocolBufferOp(DistributorOps_pb2.Operation.SET_PROCEDURAL_ANIMATION_DATA, animation_data_msg)
        distributor.add_op(owner, op)

class PenAnimalType(AnimalTypeBase):
    FACTORY_TUNABLES = {'locked_args': {'move_to_spawn_point_state_value': None, 'move_to_spawn_point_tags': None}}

class ChickAnimalType(ChickenAnimalType):

    @classproperty
    def creature_type(cls):
        return CreatureType.Chick

class HenAnimalType(ChickenAnimalType):

    @classproperty
    def creature_type(cls):
        return CreatureType.Hen

class RoosterAnimalType(ChickenAnimalType):

    @classproperty
    def creature_type(cls):
        return CreatureType.Rooster

class CowAnimalType(PenAnimalType):

    @classproperty
    def creature_type(cls):
        return CreatureType.Cow

class LlamaAnimalType(PenAnimalType):

    @classproperty
    def creature_type(cls):
        return CreatureType.Llama
