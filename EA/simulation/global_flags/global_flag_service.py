from sims4.service_manager import Service
class GlobalFlagService(Service):

    def __init__(self):
        self._flags = 0

    def add_flag(self, flag):
        self._flags |= flag

    def remove_flag(self, flag):
        self._flags &= ~flag

    def has_any_flag(self, flags):
        return bool(self._flags & flags)
