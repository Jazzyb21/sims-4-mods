import randomimport servicesfrom sims4.math import EPSILONfrom sims4.random import weighted_random_itemfrom sims4.resources import Typesfrom sims4.tuning.tunable import HasTunableSingletonFactory, AutoFactoryInit, TunableReferencefrom story_progression.story_progression_lot_selection import StoryProgressionLotSelection
class BaseCandidateSelectionFunction(HasTunableSingletonFactory, AutoFactoryInit):

    def __call__(self, demographic_sim_infos, demographic_households, demographic_zones, arc):
        if demographic_sim_infos is not None:
            for sim in tuple(demographic_sim_infos):
                household = sim.household
                rule_set = household.story_progression_rule_set
                if not household.scenario_tracker.active_scenario is not None:
                    if not sim.story_progression_tracker.can_add_arc(arc):
                        demographic_sim_infos.remove(sim)
                demographic_sim_infos.remove(sim)
        if demographic_households is not None:
            household_manager = services.household_manager()
            for household_id in tuple(demographic_households):
                household = household_manager.get(household_id)
                rule_set = household.story_progression_rule_set
                if not household.scenario_tracker.active_scenario is not None:
                    if not household.story_progression_tracker.can_add_arc(arc):
                        demographic_households.remove(household_id)
                demographic_households.remove(household_id)

class SelectSimCandidateFromDemographicListFunction(BaseCandidateSelectionFunction):

    def __call__(self, demographic_sim_infos, demographic_households, demographic_zones, required_rules):
        super().__call__(demographic_sim_infos, demographic_households, demographic_zones, required_rules)
        if not demographic_sim_infos:
            return (None, None, None)
        return (random.choice(demographic_sim_infos), None, None)

class SelectSimCandidateFromFilterFunction(BaseCandidateSelectionFunction):
    FACTORY_TUNABLES = {'sim_filter': TunableReference(description='\n            The Sim Filter that we will use in order to determine the candidate Sim.\n            ', manager=services.get_instance_manager(Types.SIM_FILTER))}

    def __call__(self, demographic_sim_infos, demographic_households, demographic_zones, arc):
        results = services.sim_filter_service().submit_filter(self.sim_filter, callback=None, blacklist_sim_ids={sim_info.sim_id for sim_info in services.active_household()}, required_story_progression_arc=arc, allow_yielding=False, gsi_source_fn=lambda : 'Sim candidate for Story Progression arc')
        if not results:
            return (None, None, None)
        return (weighted_random_item([(result.score, result.sim_info) for result in results]), None, None)

class SelectHouseholdCandidateMatchingLotFromDemographicListFunction(BaseCandidateSelectionFunction):

    def __call__(self, demographic_sim_infos, demographic_households, demographic_zones, arc):
        possible_households = list(services.household_manager().values())
        for household in tuple(possible_households):
            if household.is_active_household:
                possible_households.remove(household)
            else:
                rule_set = household.story_progression_rule_set
                if not rule_set.verify(arc.required_rules):
                    possible_households.remove(household)
                elif not household.story_progression_tracker.can_add_arc(arc):
                    possible_households.remove(household)
        if demographic_zones:
            possible_zones = demographic_zones.copy()
            if possible_zones:
                zone_id = possible_zones.pop(random.randint(0, len(possible_zones) - 1))
                templates_and_bed_data = StoryProgressionLotSelection.get_household_templates_and_bed_data(zone_id)
                (total_beds, lot_has_double_bed, lot_has_kid_bed) = templates_and_bed_data
                if total_beds <= 0:
                    pass
                else:
                    weighted_households = StoryProgressionLotSelection.get_available_households(possible_households, total_beds, lot_has_double_bed, lot_has_kid_bed)
                    if not weighted_households:
                        pass
                    else:
                        return (None, weighted_random_item(weighted_households), zone_id)
        return (None, None, None)

class SelectHouseholdWithHomeCandidateFromDemographicListBasedOnCullingScoreFunction(BaseCandidateSelectionFunction):

    def __call__(self, demographic_sim_infos, demographic_households, demographic_zones, arc):
        super().__call__(demographic_sim_infos, demographic_households, demographic_zones, arc)
        culling_service = services.get_culling_service()
        household_manager = services.household_manager()
        weighted_households = []
        for household_id in demographic_households:
            household = household_manager.get(household_id)
            if household is None:
                pass
            elif household.home_zone_id == 0:
                pass
            else:
                weight = max(culling_service.get_culling_score_for_sim_info(sim_info).score for sim_info in household)
                if weight <= 0:
                    weight = EPSILON
                weighted_households.append((1/weight, household_id))
        if not weighted_households:
            return (None, None, None)
        return (None, weighted_random_item(weighted_households), None)
