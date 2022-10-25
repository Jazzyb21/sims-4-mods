from gsi_handlers.sim_handlers import _get_sim_info_by_id
@GsiHandler('lifestyle_brand_view', lifestyle_brand_schema)
def generate_lifestyle_brand_data(sim_id:int=None):
    cur_sim_info = _get_sim_info_by_id(sim_id)
    lifestyle_brand_tracker = cur_sim_info.lifestyle_brand_tracker
    if lifestyle_brand_tracker is None:
        return {}
    entry = {'brand_name': lifestyle_brand_tracker.brand_name, 'target_market': str(lifestyle_brand_tracker.target_market), 'product': str(lifestyle_brand_tracker.product_choice), 'days_active': str(lifestyle_brand_tracker.days_active), 'next_payout': str(lifestyle_brand_tracker.get_payout_amount())}
    return entry
