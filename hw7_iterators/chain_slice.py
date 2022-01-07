from itertools import chain, islice


def chainslice(begin, end, *sequences):
    return islice(chain(*sequences), begin, end)
