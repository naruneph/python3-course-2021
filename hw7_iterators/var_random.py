from random import randint
from itertools import cycle


def randomes(it):
    all_intervals = []

    for item in it:
        interval = tuple(item)
        all_intervals.append(interval)
        yield randint(*interval)

    for interval in cycle(all_intervals):
        yield randint(*interval)
