class Lock:
    locks = {}  # lock_name : {locked_by: ... , queue: set(...)}

    # проверка доступности и одновременно захват
    def __get__(self, obj, cls):
        for lock_name in Lock.locks:
            if Lock.locks[lock_name]["locked_by"] == id(obj):
                return lock_name
            elif (
                Lock.locks[lock_name]["locked_by"] is None
                and Lock.locks[lock_name]["queue"]
            ):
                if id(obj) in Lock.locks[lock_name]["queue"]:
                    Lock.locks[lock_name]["locked_by"] = id(obj)

                    return lock_name

        return None

    # регистрация
    def __set__(self, obj, val):
        self.__delete__(obj)

        if val in Lock.locks:

            Lock.locks[val]["queue"].add(id(obj))
        else:

            Lock.locks[val] = {"locked_by": None, "queue": {id(obj)}}

    def __delete__(self, obj):
        for lock_name in Lock.locks:
            if Lock.locks[lock_name]["locked_by"] == id(obj):
                Lock.locks[lock_name]["locked_by"] = None

                Lock.locks[lock_name]["queue"].discard(id(obj))

                if not Lock.locks[lock_name]["queue"]:
                    del Lock.locks[lock_name]

                break

    @staticmethod
    def locked(cls):
        setattr(cls, "lock", Lock())

        if "__del__" in dir(cls):
            tmp = getattr(cls, "__del__")
        else:
            tmp = None

        def helper(s):
            del s.lock
            if tmp is not None:
                tmp(s)

        setattr(cls, "__del__", helper)

        return cls
