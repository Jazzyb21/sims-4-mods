import services
    outfit_change_log_enabled = False
class OutfitGenerator(OutfitGeneratorRandomizationMixin, HasTunableSingletonFactory, AutoFactoryInit):
    FACTORY_TUNABLES = {'tags': TunableSet(description='\n            The set of tags used to generate the outfit. Parts must match the\n            specified tag in order to be valid for the generated outfit.\n            ', tunable=TunableEnumWithFilter(tunable_type=Tag, filter_prefixes=('Uniform', 'OutfitCategory', 'Style', 'Situation'), default=Tag.INVALID, invalid_enums=(Tag.INVALID,), pack_safe=True))}

    def __call__(self, *args, outfit_extra_tag_set=None, **kwargs):
        tags = self.tags
        if outfit_extra_tag_set:
            tags = outfit_extra_tag_set.union(self.tags)
        self._generate_outfit(*args, tag_list=tags, **kwargs)

    @staticmethod
    def generate_outfit(outfit_generator, sim_info, outfit_category, **kwargs):
        outfit_generator.generator(sim_info, outfit_category, **kwargs)
