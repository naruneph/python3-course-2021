def joinseq(*sequences):
    iterators = [iter(it) for it in sequences]

    if not len(iterators):
        return

    values = [None] * len(iterators)

    while True:
        for i, it in enumerate(iterators):
            if values[i] is None:
                values[i] = next(it, None)

        if values.count(None) == len(values):
            return

        min_val = min(x for x in values if x is not None)
        min_idx = values.index(min_val)
        values[min_idx] = None
        yield min_val
