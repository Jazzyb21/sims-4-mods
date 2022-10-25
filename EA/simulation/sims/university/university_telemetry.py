import build_buy
class UniversityTelemetry:

    @staticmethod
    def send_university_housing_telemetry(zone_id):
        if zone_id is None:
            return
        is_university_housing = False
        if zone_id != 0:
            venue_manager = services.get_instance_manager(sims4.resources.Types.VENUE)
            venue = venue_manager.get(build_buy.get_current_venue(zone_id))
            is_university_housing = venue.is_university_housing
        with telemetry_helper.begin_hook(university_telemetry_writer, TELEMETRY_HOOK_UNIVERSITY_HOUSING) as hook:
            hook.write_bool(TELEMETRY_FIELD_IS_ON_CAMPUS_HOUSING, is_university_housing)

    @staticmethod
    def send_acceptance_telemetry(sim_age):
        with telemetry_helper.begin_hook(university_telemetry_writer, TELEMETRY_HOOK_UNIVERSITY_ACCEPTANCE) as hook:
            hook.write_enum(TELEMETRY_FIELD_SIM_AGE, sim_age)

    @staticmethod
    def send_university_enroll_telemetry(sim_info, major):
        with telemetry_helper.begin_hook(university_telemetry_writer, TELEMETRY_HOOK_UNIVERSITY_ENROLL, sim_info=sim_info) as hook:
            hook.write_int(TELEMETRY_FIELD_UNIVERSITY_MAJOR, major.guid64)

    @staticmethod
    def send_university_term_telemetry(sim_info, major, gpa):
        with telemetry_helper.begin_hook(university_telemetry_writer, TELEMETRY_HOOK_UNIVERSITY_TERM, sim_info=sim_info) as hook:
            hook.write_int(TELEMETRY_FIELD_UNIVERSITY_MAJOR, major.guid64)
            hook.write_float(TELEMETRY_FIELD_TERM_GPA, gpa)

    @staticmethod
    def send_university_course_telemetry(sim_info, major, course_data, grade):
        with telemetry_helper.begin_hook(university_telemetry_writer, TELEMETRY_HOOK_UNIVERSITY_COURSE, sim_info=sim_info) as hook:
            hook.write_int(TELEMETRY_FIELD_UNIVERSITY_MAJOR, major.guid64)
            hook.write_int(TELEMETRY_FIELD_COURSE_ID, course_data.guid64)
            hook.write_int(TELEMETRY_FIELD_COURSE_GRADE, grade)

    @staticmethod
    def send_university_tuition_telemetry(sim_info, tuition_cost, is_using_loan):
        with telemetry_helper.begin_hook(university_telemetry_writer, TELEMETRY_HOOK_UNIVERSITY_TUITION, sim_info=sim_info) as hook:
            hook.write_int(TELEMETRY_FIELD_TUITION_COST, tuition_cost)
            hook.write_bool(TELEMETRY_FIELD_IS_USING_LOAN, is_using_loan)
