import _signal
    _IntEnum._convert('Sigmasks', __name__, lambda name: name in ('SIG_BLOCK', 'SIG_UNBLOCK', 'SIG_SETMASK'))
def _int_to_enum(value, enum_klass):
    try:
        return enum_klass(value)
    except ValueError:
        return value

def _enum_to_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return value

@_wraps(_signal.signal)
def signal(signalnum, handler):
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
    return _int_to_enum(handler, Handlers)

@_wraps(_signal.getsignal)
def getsignal(signalnum):
    handler = _signal.getsignal(signalnum)
    return _int_to_enum(handler, Handlers)


    @_wraps(_signal.pthread_sigmask)
    def pthread_sigmask(how, mask):
        sigs_set = _signal.pthread_sigmask(how, mask)
        return set(_int_to_enum(x, Signals) for x in sigs_set)

    pthread_sigmask.__doc__ = _signal.pthread_sigmask.__doc__

    @_wraps(_signal.sigpending)
    def sigpending():
        sigs = _signal.sigpending()
        return set(_int_to_enum(x, Signals) for x in sigs)


    @_wraps(_signal.sigwait)
    def sigwait(sigset):
        retsig = _signal.sigwait(sigset)
        return _int_to_enum(retsig, Signals)

    sigwait.__doc__ = _signal.sigwait