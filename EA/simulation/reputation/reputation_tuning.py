from sims4.tuning.tunable import TunablePackSafeReference
class ReputationTunables:
    REPUTATION_RANKED_STATISTIC = TunablePackSafeReference(description='\n        The ranked statistic that is to be used for tracking reputation progress.\n        \n        This should not need to be tuned at all. If you think you need to tune\n        this please speak with a GPE before doing so.\n        ', manager=services.get_instance_manager(sims4.resources.Types.STATISTIC), class_restrictions=('RankedStatistic',), export_modes=(ExportModes.ClientBinary,))
