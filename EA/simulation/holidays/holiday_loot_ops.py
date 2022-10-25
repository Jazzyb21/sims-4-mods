import services
class HolidaySearchLootOp(BaseTargetedLootOperation):

    def _apply_to_subject_and_target(self, subject, target, resolver):
        active_household = services.active_household()
        if active_household is None:
            return
        active_holiday_id = active_household.holiday_tracker.active_holiday_id
        if active_holiday_id is None:
            return
        for drama_node in services.drama_scheduler_service().active_nodes_gen():
            if drama_node.drama_node_type != DramaNodeType.HOLIDAY:
                pass
            elif drama_node.holiday_id != active_holiday_id:
                pass
            elif drama_node.drama_node_type == DramaNodeType.HOLIDAY:
                drama_node.search_obj(target.id)
                break
