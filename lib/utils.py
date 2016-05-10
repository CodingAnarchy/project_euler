import operator
import math


def prod(iterable):
    return reduce(operator.mul, iterable)


def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1, 1))


def sum_digits(n):
    return sum([int(i) for i in str(n)])


def sum_factors(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n/i
    if t == int(t): s -= t    #correct s if n is a perfect square
    return s
