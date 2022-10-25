import servicesfrom sims4.resources import Typesfrom sims4.tuning.tunable import TunableReference
class SectionalSofaTuning:
    SECTIONAL_SOFA_OBJECT_DEF = TunableReference(description='\n        Catalog definition for the sectional sofa object.\n        ', manager=services.get_instance_manager(Types.OBJECT))
