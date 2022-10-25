import os
def _get_proxy(obj, get_only=True):

    class Proxy(object):

        def __getattr__(self, name):
            return getattr(obj, name)

    if not get_only:

        def __setattr__(self, name, value):
            setattr(obj, name, value)

        def __delattr__(self, name):
            delattr(obj, name)

        Proxy.__setattr__ = __setattr__
        Proxy.__delattr__ = __delattr__
    return Proxy()

class Foo(object):

    def __init__(self, a):
        pass

    def f(self, a):
        pass

    def g(self):
        pass

    foo = 'bar'

    class Bar(object):

        def a(self):
            pass

def function(a, b=Foo):
    pass

class Container(object):

    def __init__(self):
        self.values = {}

    def __getitem__(self, name):
        return self.values[name]

    def __setitem__(self, name, value):
        self.values[name] = value

    def __delitem__(self, name):
        del self.values[name]

    def __iter__(self):
        return iter(self.values)
