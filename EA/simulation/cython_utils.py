import cythonimport sims4.logfrom postures.posture_specs import cython_logfrom sims4.log import Loggerlogger = Logger('CythonUtils')if cython.compiled:
    cython_log.always('CYTHON cython_utils is imported!', color=sims4.log.LEVEL_WARN)
else:
    cython_log.always('Pure Python cython_utils is imported!', color=sims4.log.LEVEL_WARN)if not cython.compiled:
    from cython_utils_ph import *