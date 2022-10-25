from sims4.tuning.instance_manager import InstanceManagerimport sims4.loglogger = sims4.log.Logger('StatisticInstanceManager')
class StatisticInstanceManager(InstanceManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._skills = []

    def register_tuned_class(self, instance, resource_key):
        super().register_tuned_class(instance, resource_key)
        if instance.is_skill:
            self._skills.append(instance)

    def create_class_instances(self):
        self._skills = []
        super().create_class_instances()

        def key(cls):
            return cls.__name__.lower()

        self._skills = tuple(sorted(self._skills, key=key))

    def all_skills_gen(self):
        yield from self._skills
