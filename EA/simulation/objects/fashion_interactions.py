from interactions.base.immediate_interaction import ImmediateSuperInteractionfrom sims4.localization import TunableLocalizedStringFactoryfrom sims4.tuning.tunable import OptionalTunable, TunableVariantfrom sims4.utils import flexmethodfrom singletons import DEFAULTfrom ui.ui_dialog_generic import UiDialogTextInputOkCancel, UiDialogTextInputOkimport element_utilsimport servicesimport sims4.logimport sims4.resourceslogger = sims4.log.Logger('Interactions')
class SetOutfitPriceImmediateInteraction(ImmediateSuperInteraction):
    TEXT_INPUT_CUSTOM_SALE_PRICE = 'custom_sale_price'
    INSTANCE_TUNABLES = {'display_name_sale_price': OptionalTunable(TunableLocalizedStringFactory(description="\n            If set, this localized string will be used as the interaction's \n            display name if the object has been previously renamed.\n            ")), 'sale_price_dialog': TunableVariant(description='\n            The rename dialog to show when running this interaction.\n            ', ok_dialog=UiDialogTextInputOk.TunableFactory(text_inputs=TEXT_INPUT_CUSTOM_SALE_PRICE), ok_cancel_dialog=UiDialogTextInputOkCancel.TunableFactory(text_inputs=TEXT_INPUT_CUSTOM_SALE_PRICE))}

    @flexmethod
    def _get_name(cls, inst, target=DEFAULT, context=DEFAULT, **kwargs):
        inst_or_cls = inst if inst is not None else cls
        target = inst.target if inst is not None else target
        if inst_or_cls.display_name_sale_price is not None and target.has_custom_name():
            display_name = inst_or_cls.display_name_sale_price
        else:
            display_name = inst_or_cls.display_name
        return inst_or_cls.create_localized_string(display_name, target=target, context=context, **kwargs)

    def _run_interaction_gen(self, timeline):
        target_object_fashion_marketplace_component = self.target.object_fashion_marketplace_component
        if target_object_fashion_marketplace_component is None:
            logger.error('Cannot set price on an object without a fashion_marketplace component.')
            return False

        def on_response(dialog):
            sale_price = dialog.text_input_responses.get(self.TEXT_INPUT_CUSTOM_SALE_PRICE)
            if not (dialog.accepted and sale_price.isnumeric()):
                return
            target = self.target
            if target is not None:
                if sale_price is not None:
                    target_object_fashion_marketplace_component.set_sale_price_override(int(sale_price))
                self._update_ui_metadata(target)
            sequence = self._build_outcome_sequence()
            services.time_service().sim_timeline.schedule(element_utils.build_element(sequence))

        dialog = self.sale_price_dialog(self.sim, self.get_resolver())
        dialog.show_dialog(on_response=on_response)
        return True

    def build_outcome(self):
        pass

    def _update_ui_metadata(self, updated_object):
        if not updated_object.on_hovertip_requested():
            updated_object.update_ui_metadata()
        current_inventory = updated_object.get_inventory()
        if current_inventory is not None:
            current_inventory.push_inventory_item_update_msg(updated_object)
