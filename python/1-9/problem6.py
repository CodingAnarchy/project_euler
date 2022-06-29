# coding=utf-8
"""
The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and
the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""


def squared_sum(n):
    s = ((n + 1) * n) / 2
    return s ** 2


def sum_squares(n):
    return ((2 * n + 1) * (n + 1) * n) / 6

print(squared_sum(100) - sum_squares(100))
