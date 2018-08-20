def gen(iterable):
    try:
        for items in iterable:
            try:
                yield from gen(items)
            except:
                yield iterable
    except:
        if iterable is None:
            return
        yield iterable


def flatten(iterable):
    return list(gen(iterable))