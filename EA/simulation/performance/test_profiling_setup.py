import profile_utilsimport servicesimport cachesfrom sims.sim_info_tests import TraitTestfrom weather.weather_enums import WeatherTypefrom weather.weather_tests import WeatherTypeTest
class TestProfilingSetup:
    tests_to_run = {}

    @staticmethod
    @profile_utils.profile_function(output_filename='tests_data')
    def start_tests(number_of_runs, clear_ratio):
        TestProfilingSetup._init_tests()
        profile_utils.add_string('number of runs : {}, clear ratio : {}'.format(number_of_runs, clear_ratio))
        for test in TestProfilingSetup.tests_to_run:
            args = TestProfilingSetup.tests_to_run[test]
            profile_utils.sub_time_start()
            for iteration in range(number_of_runs):
                if iteration % clear_ratio == 0:
                    caches.skip_cache_once = True
                test.default(**args)
            profile_utils.sub_time_end('test {}'.format(test))

    @staticmethod
    def _init_tests():
        TestProfilingSetup.tests_to_run.clear()
        TestProfilingSetup._init_weather_type_test()
        TestProfilingSetup._init_trait_test()

    @staticmethod
    def _init_weather_type_test():
        weather_type_test = WeatherTypeTest.TunableFactory(locked_args={'weather_types': frozenset({WeatherType.AnyRain})})
        TestProfilingSetup.tests_to_run[weather_type_test] = {}

    @staticmethod
    def _init_trait_test():
        active_sim_info = services.active_sim_info()
        if active_sim_info:
            traits = active_sim_info.trait_tracker.equipped_traits
            trait_test = TraitTest.TunableFactory(locked_args={'whitelist_traits': frozenset(traits)})
            TestProfilingSetup.tests_to_run[trait_test] = {'test_targets': (active_sim_info,)}
