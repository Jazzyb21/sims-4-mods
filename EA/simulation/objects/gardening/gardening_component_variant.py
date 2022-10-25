from objects.gardening.gardening_component_crop_fruit import GardeningCropFruitComponentfrom objects.gardening.gardening_component_crop_plant import GardeningCropPlantComponentfrom objects.gardening.gardening_component_fruit import GardeningFruitComponentfrom objects.gardening.gardening_component_plant import GardeningPlantComponentfrom objects.gardening.gardening_component_shoot import GardeningShootComponentfrom sims4.tuning.tunable import TunableVariant
class TunableGardeningComponentVariant(TunableVariant):

    def __init__(self, **kwargs):
        super().__init__(fruit_component=GardeningFruitComponent.TunableFactory(), plant_component=GardeningPlantComponent.TunableFactory(), crop_fruit_component=GardeningCropFruitComponent.TunableFactory(), crop_plant_component=GardeningCropPlantComponent.TunableFactory(), shoot=GardeningShootComponent.TunableFactory(), locked_args={'disabled': None}, default='disabled', **kwargs)
