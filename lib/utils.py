import operator


def prod(iterable):
    return reduce(operator.mul, iterable)
