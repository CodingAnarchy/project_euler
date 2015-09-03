import time
from lib.utils import sum_factors

start = time.time()

limit = 28123
abundant = set()
for i in range(1, limit):
    if sum_factors(i) > i:
        abundant.add(i)

pairs = set()
for x in abundant:
    for y in abundant:
        pairs.add(x + y)

numbers = set(range(1, limit))

total = sum(numbers - pairs)
elapsed = time.time() - start
print "found %s in %s seconds" % (total, elapsed)
