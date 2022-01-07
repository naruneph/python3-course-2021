class Dsc:
    def __get__(self, obj, cls):
        if "__len__" in dir(obj):
            return len(obj)
        elif "__abs__" in dir(obj):
            return abs(obj)
        return 0


def sizer(base_cls):
    class new_cls(base_cls):
        size = Dsc()
    return new_cls
