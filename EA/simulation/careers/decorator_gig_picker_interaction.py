from careers.career_enums import DecoratorGigType, DecoratorGigLotTypefrom distributor.rollback import ProtocolBufferRollbackfrom distributor.shared_messages import build_icon_info_msgfrom drama_scheduler.drama_node_picker_interaction import DramaNodePickerInteractionfrom interactions.utils.tunable_icon import TunableIconFactoryfrom sims4.localization import TunableLocalizedStringfrom sims4.tuning.tunable import TunableList, TunableTuple, TunableEnumEntry, Tunablefrom sims4.tuning.tunable_base import GroupNamesfrom ui.ui_dialog_picker import UiObjectPicker
class UiDecoratorPicker(UiObjectPicker):
    FACTORY_TUNABLES = {'filter_categories': TunableList(description='\n            The categories to display in the filter for this picker.\n            ', tunable=TunableTuple(filter_category=TunableEnumEntry(tunable_type=DecoratorGigType, default=DecoratorGigType.ROOM_RENOVATION), icon=TunableIconFactory(), category_name=TunableLocalizedString())), 'secondary_categories': TunableList(description='\n            The categories to display in the dropdown for this picker.\n            ', tunable=TunableTuple(dropdown_category=TunableEnumEntry(tunable_type=DecoratorGigLotType, default=DecoratorGigLotType.RESIDENTIAL), icon=TunableIconFactory(), category_name=TunableLocalizedString())), 'use_secondary_dropdown_filter': Tunable(description='\n           Should secondary categories be presented in a dropdown\n           ', tunable_type=bool, default=False)}

    def _build_customize_picker(self, picker_data):
        with ProtocolBufferRollback(picker_data.filter_data) as filter_data_list:
            for category in self.filter_categories:
                with ProtocolBufferRollback(filter_data_list.filter_data) as category_data:
                    category_data.tag_type = category.filter_category
                    build_icon_info_msg(category.icon(None), None, category_data.icon_info)
                    category_data.description = category.category_name
            filter_data_list.use_dropdown_filter = self.use_dropdown_filter
        with ProtocolBufferRollback(picker_data.filter_data) as filter_data_list2:
            for category in self.secondary_categories:
                with ProtocolBufferRollback(filter_data_list2.filter_data) as category_data:
                    category_data.tag_type = category.dropdown_category
                    build_icon_info_msg(category.icon(None), None, category_data.icon_info)
                    category_data.description = category.category_name
            filter_data_list2.use_dropdown_filter = self.use_secondary_dropdown_filter
        picker_data.object_picker_data.num_columns = self.num_columns
        for row in self.picker_rows:
            row_data = picker_data.object_picker_data.row_data.add()
            row.populate_protocol_buffer(row_data)

class DecoratorGigPickerInteraction(DramaNodePickerInteraction):
    INSTANCE_TUNABLES = {'picker_dialog': UiDecoratorPicker.TunableFactory(description='\n            The odd job picker dialog.\n            ', tuning_group=GroupNames.PICKERTUNING)}
