import operator
import math


def prod(iterable):
    return reduce(operator.mul, iterable)


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1, 1))


def sum_digits(n):
    return sum([int(i) for i in str(n)])


def sum_factors(n):
    return sum([i for i in range(1, n) if n % i == 0])
