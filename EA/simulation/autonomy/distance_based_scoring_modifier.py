import sims4logger = sims4.log.Logger('DistanceBasedScoringModifier', default_owner='uviswavasu')
class DistanceToObjectBasedScoringModifier:

    def __init__(self, modifier):
        self.object_tag = modifier.object_tag
        self._distance_to_multiplier_map = []
        for mapping in modifier.distance_to_multiplier_map:
            self._distance_to_multiplier_map.append(tuple((mapping.distance_threshold, mapping.multiplier)))
        self._distance_to_multiplier_map.sort()
        self._outside_threshold_multiplier = modifier.outside_threshold_multiplier
        self._reference_count = 1

    def get_multiplier_for_distance(self, dist):
        for (distance, multiplier) in self._distance_to_multiplier_map:
            if dist < distance:
                return multiplier**self._reference_count
        return self._outside_threshold_multiplier**self._reference_count

    def increase_ref_count(self):
        self._reference_count += 1

    def decrease_ref_count(self):
        self._reference_count -= 1

    def get_ref_count(self):
        return self._reference_count
