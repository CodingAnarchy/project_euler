import operator


def prod(iterable):
    return reduce(operator.mul, iterable)


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1, 1))


def sum_digits(n):
    return sum([int(i) for i in str(n)])
