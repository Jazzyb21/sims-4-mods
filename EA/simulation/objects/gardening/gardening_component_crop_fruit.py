from crafting.crafting_tunable import CraftingTuningfrom objects.components.spoilable_object_mixin import SpoilableObjectMixinfrom objects.gardening.gardening_component_base_fruit import _GardeningBaseFruitComponentfrom objects.gardening.gardening_tuning import GardeningTuningfrom objects.hovertip import TooltipFieldsCompletefrom protocolbuffers import SimObjectAttributes_pb2 as protocolsfrom objects.components import typesimport objects.components.typesimport sims4.logimport sims4.mathfrom sims4.tuning.tunable import Tunablelogger = sims4.log.Logger('Gardening', default_owner='miking')
class GardeningCropFruitComponent(SpoilableObjectMixin, _GardeningBaseFruitComponent, component_name=objects.components.types.GARDENING_COMPONENT, persistence_key=protocols.PersistenceMaster.PersistableData.GardeningComponent):
    FACTORY_TUNABLES = {'weight_money_multiplier': Tunable(description='\n            The weight of the crop will be multiplied by this number then the\n            result of that multiplication will be added to the base value of\n            the crop.\n            ', tunable_type=float, default=1)}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def on_add(self, *args, **kwargs):
        self.spoilable_on_add()
        return super().on_add(*args, **kwargs)

    def on_remove(self, *args, **kwargs):
        self.spoilable_on_remove()
        self.spoilable_on_remove_hovertip()

    def on_state_changed(self, state, old_value, new_value, from_init):
        fruit = self.owner
        self.spoilable_on_object_state_change(fruit, state, old_value, new_value, GardeningTuning.QUALITY_STATE_VALUE)
        if self.object_is_spoiled(fruit):
            self.owner.update_tooltip_field(TooltipFieldsComplete.quality_description, CraftingTuning.SPOILED_STRING)
            self.owner.update_tooltip_field(TooltipFieldsComplete.spoiled_time, 0)
        self.update_hovertip()

    def on_hovertip_requested(self):
        self.spoilable_on_add_hovertip(None, None)
        return super().on_hovertip_requested()

    def save(self, persistence_master_message):
        self.spoilable_pre_save()
        return super().save(persistence_master_message)

    def update_crop_cost(self, crop_weight):
        self.owner.base_value += int(crop_weight*self.weight_money_multiplier)
        self.owner.update_object_tooltip()
