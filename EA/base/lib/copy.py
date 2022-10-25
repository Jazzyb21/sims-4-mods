import types
class Error(Exception):
    pass

    from org.python.core import PyStringMap
except ImportError:
    PyStringMap = None
def copy(x):
    cls = type(x)
    copier = _copy_dispatch.get(cls)
    if copier:
        return copier(x)
    try:
        issc = issubclass(cls, type)
    except TypeError:
        issc = False
    if issc:
        return _copy_immutable(x)
    copier = getattr(cls, '__copy__', None)
    if copier:
        return copier(x)
    reductor = dispatch_table.get(cls)
    if reductor:
        rv = reductor(x)
    else:
        reductor = getattr(x, '__reduce_ex__', None)
        if reductor:
            rv = reductor(4)
        else:
            reductor = getattr(x, '__reduce__', None)
            if reductor:
                rv = reductor()
            else:
                raise Error('un(shallow)copyable object of type %s' % cls)
    if isinstance(rv, str):
        return x
    return _reconstruct(x, None, rv)

def _copy_immutable(x):
    return x

    d[t] = _copy_immutable
    d[t] = _copy_immutable
    d[PyStringMap] = PyStringMap.copy
def deepcopy(x, memo=None, _nil=[]):
    if memo is None:
        memo = {}
    d = id(x)
    y = memo.get(d, _nil)
    if y is not _nil:
        return y
    cls = type(x)
    copier = _deepcopy_dispatch.get(cls)
    if copier:
        y = copier(x, memo)
    else:
        try:
            issc = issubclass(cls, type)
        except TypeError:
            issc = 0
        if issc:
            y = _deepcopy_atomic(x, memo)
        else:
            copier = getattr(x, '__deepcopy__', None)
            if copier:
                y = copier(memo)
            else:
                reductor = dispatch_table.get(cls)
                if reductor:
                    rv = reductor(x)
                else:
                    reductor = getattr(x, '__reduce_ex__', None)
                    if reductor:
                        rv = reductor(4)
                    else:
                        reductor = getattr(x, '__reduce__', None)
                        if reductor:
                            rv = reductor()
                        else:
                            raise Error('un(deep)copyable object of type %s' % cls)
                if isinstance(rv, str):
                    y = x
                else:
                    y = _reconstruct(x, memo, rv)
    if y is not x:
        memo[d] = y
        _keep_alive(x, memo)
    return y

def _deepcopy_atomic(x, memo):
    return x

    d[types.CodeType] = _deepcopy_atomic
except AttributeError:
    pass
def _deepcopy_list(x, memo, deepcopy=deepcopy):
    y = []
    memo[id(x)] = y
    append = y.append
    for a in x:
        append(deepcopy(a, memo))
    return y

def _deepcopy_tuple(x, memo, deepcopy=deepcopy):
    y = [deepcopy(a, memo) for a in x]
    try:
        return memo[id(x)]
    except KeyError:
        pass
    for (k, j) in zip(x, y):
        if k is not j:
            y = tuple(y)
            break
    y = x
    return y

def _deepcopy_dict(x, memo, deepcopy=deepcopy):
    y = {}
    memo[id(x)] = y
    for (key, value) in x.items():
        y[deepcopy(key, memo)] = deepcopy(value, memo)
    return y

    d[PyStringMap] = _deepcopy_dict
def _deepcopy_method(x, memo):
    return type(x)(x.__func__, deepcopy(x.__self__, memo))

def _keep_alive(x, memo):
    try:
        memo[id(memo)].append(x)
    except KeyError:
        memo[id(memo)] = [x]

def _reconstruct(x, memo, func, args, state=None, listiter=None, dictiter=None, deepcopy=deepcopy):
    deep = memo is not None
    if args:
        args = (deepcopy(arg, memo) for arg in args)
    y = func(*args)
    if deep and deep:
        memo[id(x)] = y
    if state is not None:
        if deep:
            state = deepcopy(state, memo)
        if hasattr(y, '__setstate__'):
            y.__setstate__(state)
        else:
            if isinstance(state, tuple) and len(state) == 2:
                (state, slotstate) = state
            else:
                slotstate = None
            if state is not None:
                y.__dict__.update(state)
            if slotstate is not None:
                for (key, value) in slotstate.items():
                    setattr(y, key, value)
    if listiter is not None:
        if deep:
            for item in listiter:
                item = deepcopy(item, memo)
                y.append(item)
        else:
            for item in listiter:
                y.append(item)
    if dictiter is not None:
        if deep:
            for (key, value) in dictiter:
                key = deepcopy(key, memo)
                value = deepcopy(value, memo)
                y[key] = value
        else:
            for (key, value) in dictiter:
                y[key] = value
    return y
