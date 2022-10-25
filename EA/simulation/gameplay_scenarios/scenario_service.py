import servicesfrom sims4.service_manager import Service
class ScenarioService(Service):

    def update(self):
        active_household = services.active_household()
        if active_household is not None:
            scenario_tracker = active_household.scenario_tracker
            if scenario_tracker is not None and scenario_tracker.active_scenario is not None:
                scenario_tracker.active_scenario.update()
