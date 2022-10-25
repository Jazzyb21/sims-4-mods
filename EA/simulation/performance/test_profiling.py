
class ProfileMetrics:

    def __init__(self, is_test_set=False):
        self.count = 0
        self.resolve_time = 0
        self.test_time = 0
        self.max_time = 0
        self.is_test_set = is_test_set

    def get_total_time(self, include_test_set=True):
        if self.is_test_set and include_test_set:
            return self.resolve_time + self.test_time
        return self.resolve_time

    def get_average_time(self, include_test_set=True):
        if self.count == 0:
            return 0
        total_time = self.get_total_time(include_test_set=include_test_set)
        if total_time == 0:
            return 0
        return total_time/self.count

    def get_max_time(self):
        return self.max_time

    def update(self, resolve_time, test_time):
        self.count += 1
        self.resolve_time += resolve_time
        self.test_time += test_time
        total_time = test_time + resolve_time
        if total_time > self.max_time:
            self.max_time = total_time

class TestProfileRecord:

    def __init__(self, is_test_set=False):
        self.metrics = ProfileMetrics(is_test_set=is_test_set)
        self.resolvers = dict()

def record_profile_metrics(profile, profile_subject_name, resolver_name, key_name, resolve_time, test_time, is_test_set=False):
    record = profile.get(profile_subject_name)
    if record is None:
        record = TestProfileRecord(is_test_set=is_test_set)
        profile[profile_subject_name] = record
    record.metrics.update(resolve_time, test_time)
    resolver_dict = record.resolvers.get(resolver_name)
    if resolver_dict is None:
        resolver_dict = dict()
        record.resolvers[resolver_name] = resolver_dict
    if key_name is None:
        key_name = 'Key'
    metrics = resolver_dict.get(key_name)
    if metrics is None:
        metrics = ProfileMetrics(is_test_set=is_test_set)
        resolver_dict[key_name] = metrics
    metrics.update(resolve_time, test_time)
