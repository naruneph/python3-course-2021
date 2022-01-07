from functools import wraps


def counter(f):

    @wraps(f)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        return f(*args, **kwargs)

    wrapper.count = 0

    def counter():
        return wrapper.count

    wrapper.counter = counter

    return wrapper
