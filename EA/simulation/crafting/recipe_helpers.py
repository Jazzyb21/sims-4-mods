from _collections import defaultdictimport servicesimport sims4with sims4.reload.protected(globals()):
    RECIPE_TAG_TO_TUNING_ID_MAP = defaultdict(set)
def get_recipes_matching_tag(tag):
    manager = services.get_instance_manager(sims4.resources.Types.RECIPE)
    recipe_guids = RECIPE_TAG_TO_TUNING_ID_MAP.get(tag)
    if recipe_guids:
        return list(manager.get(recipe_guid) for recipe_guid in recipe_guids)
    return []
