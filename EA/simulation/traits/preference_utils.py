import servicesimport sims4.resourcesfrom traits.preference_enums import PreferenceTypes
def preferences_gen():
    trait_manager = services.get_instance_manager(sims4.resources.Types.TRAIT)
    if trait_manager is None:
        return
    for trait in trait_manager.types.values():
        if trait.is_preference_trait:
            yield trait

def get_preferences_by_category(category):
    return [p for p in preferences_gen() if p.preference_category is category]
