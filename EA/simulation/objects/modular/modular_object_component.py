from objects.components import Component, types
class ModularObjectComponent(Component, component_name=types.MODULAR_OBJECT_COMPONENT, persistence_key=protocols.PersistenceMaster.PersistableData.ModularObjectComponent):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._piece_ids = None
        self._piece_provided_affordances = None

    def track_modular_piece_ids(self, piece_ids):
        self._piece_ids = tuple(piece_ids)

    @property
    def modular_piece_ids(self):
        if self._piece_ids:
            return self._piece_ids
        return ()

    def set_piece_provided_affordances(self, affordances):
        self._piece_provided_affordances = affordances

    @property
    def piece_provided_affordances(self):
        if self._piece_provided_affordances:
            return self._piece_provided_affordances
        return ()

    def component_super_affordances_gen(self, **kwargs):
        yield from self._piece_provided_affordances

    def save(self, persistence_master_message):
        if not self._piece_ids:
            return
        persistable_data = protocols.PersistenceMaster.PersistableData()
        persistable_data.type = protocols.PersistenceMaster.PersistableData.ModularObjectComponent
        modular_object_component_data = persistable_data.Extensions[protocols.PersistableModularObjectComponent.persistable_data]
        modular_object_component_data.piece_ids.extend(self._piece_ids)
        persistence_master_message.data.extend([persistable_data])

    def load(self, persistable_data):
        modular_object_component_data = persistable_data.Extensions[protocols.PersistableModularObjectComponent.persistable_data]
        self._piece_ids = []
        for piece_id in modular_object_component_data.piece_ids:
            self._piece_ids.append(piece_id)
