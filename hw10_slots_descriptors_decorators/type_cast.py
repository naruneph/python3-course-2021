import functools


def cast(type):
    def wrapper(f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            return type(f(*args, **kwargs))
        return func
    return wrapper
