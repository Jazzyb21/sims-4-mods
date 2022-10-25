from celebrity_fans.fan_tuning import FanTuning
class FannableCelebritySimsSituation(SimBackgroundSituation):

    def _on_set_sim_job(self, sim, job):
        super()._on_set_sim_job(sim, job)
        sim.append_tags(set((FanTuning.FAN_TARGETTING_TAG,)))
