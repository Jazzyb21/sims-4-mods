from _weakrefset import WeakSetimport servicesimport sims4.logimport sims4.reloadlogger = sims4.log.Logger('Pool Utils', default_owner='skorman')with sims4.reload.protected(globals()):
    cached_pool_objects = WeakSet()POOL_LANDING_SURFACE = 'Water'
def get_main_pool_objects_gen():
    yield from cached_pool_objects

def get_pool_by_block_id(block_id):
    for pool in get_main_pool_objects_gen():
        if pool.block_id == block_id:
            return pool
    logger.error('No Pool Matching block Id: {}', block_id, owner='camilogarcia')
