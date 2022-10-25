import operatorimport randomfrom sims4.tuning.tunable import AutoFactoryInit, HasTunableSingletonFactory, Tunable, TunableVariantfrom sims4.utils import flexmethodimport servicesimport sims4.loglogger = sims4.log.Logger('AutoPick', default_owner='jdimailig')
class AutoPick(TunableVariant):

    def __init__(self, **kwargs):
        super().__init__(randomized_pick=AutoPickRandom.TunableFactory(), best_object_relationship=AutoPickBestObjectRelationship.TunableFactory(), locked_args={'disabled': False}, default='disabled', **kwargs)

class AutoPickRandom(HasTunableSingletonFactory, AutoFactoryInit):

    @flexmethod
    def perform_auto_pick(cls, inst, choices):
        return random.choice(choices)

class AutoPickBestObjectRelationship(HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'exclude_no_relationships': Tunable(description="\n            If checked, objects that haven't had a relationship with the Sim are excluded.\n            ", tunable_type=bool, default=True)}

    def perform_auto_pick(self, choices):
        household = services.active_household()
        if household is None:
            return
        sim_ids = tuple(sim_info.id for sim_info in household.sim_info_gen())
        obj_rel_tuples_list = []
        for choice in choices:
            obj_rel_tuples_list.extend(self._get_obj_rel_tuples_for_sims(choice, sim_ids))
        if not obj_rel_tuples_list:
            return
        return max(obj_rel_tuples_list, key=operator.itemgetter(1))[0]

    def _get_obj_rel_tuples_for_sims(self, obj, sim_ids):
        tuple_list = []
        comp = obj.objectrelationship_component
        if comp is None:
            return tuple_list
        for sim_id in sim_ids:
            if self.exclude_no_relationships:
                if comp.has_relationship(sim_id):
                    tuple_list.append((obj, comp.get_relationship_value(sim_id)))
            tuple_list.append((obj, comp.get_relationship_value(sim_id)))
        return tuple_list
