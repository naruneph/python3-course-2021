class Tester:
    def __init__(self, func):
        self.func = func

    def __call__(self, suite, allowed=[]):
        isallowed = False
        isnotallowed = False

        for item in suite:
            try:
                self.func(*item)
            except tuple(allowed):
                isallowed = True
            except Exception:
                isnotallowed = True

        if isnotallowed:
            return 1
        elif isallowed:
            return -1
        else:
            return 0
