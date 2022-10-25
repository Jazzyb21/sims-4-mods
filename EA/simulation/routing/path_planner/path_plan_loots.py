import sims4
class UpdateAllowedWadingDepths(BaseLootOperation):
    USE_TUNED_FLAGS = 1
    FACTORY_TUNABLES = {'allowed_wading_depths': TunableVariant(specific_flags=OptionalTunable(TunableEnumFlags(description='\n                    Flags that define the wading depth this agent is able to route\n                    through. Each flag has a specific depth assigned to it. \n    \n                    If disabled, the agent will not be allowed to wade through \n                    water entities that consider these flags. Currently these flags \n                    are only considered when routing through ponds.\n    \n                    WADING_DEEP  = 0.7m\n                    WADING_MEDIUM  = 0.5m\n                    WADING_SHALLOW  = 0.35m\n                    WADING_VERY_SHALLOW = 0.15m\n                    ', enum_type=WadingFootprintKeyMaskBits, default=WadingFootprintKeyMaskBits.WADING_MEDIUM)), locked_args={'use_tuned_flags': USE_TUNED_FLAGS}, default='use_tuned_flags')}

    def __init__(self, allowed_wading_depths, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._allowed_wading_depths = allowed_wading_depths

    def _apply_to_subject_and_target(self, subject, target, resolver):
        if subject.is_sim:
            subject = subject.get_sim_instance(allow_hidden_flags=ALL_HIDDEN_REASONS)
            if subject is None:
                return
        routing_component = subject.routing_component
        if routing_component is None:
            logger.error('Trying to update the allowed wading depth for object {}, which does not have a routing component', subject)
            return
        pathplan_context = routing_component.pathplan_context
        if pathplan_context is None:
            logger.error('Trying to update the allowed wading depth for object {}, which does not have a path plan context.', subject)
        if self._allowed_wading_depths == self.USE_TUNED_FLAGS:
            result = pathplan_context.try_update_allowed_wading_depth_flags(pathplan_context._allowed_wading_depths)
        else:
            result = pathplan_context.try_update_allowed_wading_depth_flags(self._allowed_wading_depths)
        if not result:
            logger.error('Trying to update the allowed wading depth for object {}, but the new flags ({}) may cause them to get stuck based on their current intended location {}.', subject, self._allowed_wading_depths, subject.intended_location)
