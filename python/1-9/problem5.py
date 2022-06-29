"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from lib.primes import multiplicity

mults = multiplicity(20)
result = 1
for k, v in mults.iteritems():
    result *= k ** v
print(result)
