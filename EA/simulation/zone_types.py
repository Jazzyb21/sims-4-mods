import enum
class ZoneState(enum.Int, export=False):
    ZONE_INIT = 0
    OBJECTS_LOADED = 1
    CLIENT_CONNECTED = 2
    HOUSEHOLDS_AND_SIM_INFOS_LOADED = 3
    ALL_SIMS_SPAWNED = 4
    HITTING_THEIR_MARKS = 5
    RUNNING = 6
    SHUTDOWN_STARTED = 7
