import functools


def decorator_function(ags):
    def wrapper(f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            val = f(*args, **kwargs)
            return DivStr(val) if type(val) is str else val
        return func

    for key, value in str.__dict__.items():
        if callable(value) and key not in {
            '__floordiv__',
            '__mod__',
            '__class__',
            '__new__',
            '__getattribute__',
            '__getattr__',
            '__str__'
        }:
            setattr(ags, key, wrapper(value))
    return ags


@decorator_function
class DivStr(str):
    def __floordiv__(self, substr_cnt):
        substr_len = len(self) // substr_cnt
        if substr_len == 0:
            return ['' for i in range(substr_cnt)]
        return [self[i:i + substr_len] for i in range(0, substr_len * substr_cnt, substr_len)]

    def __mod__(self, substr_cnt):
        mod_len = len(self) - (len(self) // substr_cnt) * substr_cnt
        if mod_len == 0:
            return DivStr("")
        return DivStr(self[-mod_len:])
