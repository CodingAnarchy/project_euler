import time
from lib.utils import sum_factors

start = time.time()

limit,total = 28123, 0
abundant = set()
for i in xrange(1, limit):
    if sum_factors(i) > i:
        abundant.add(i)
    if not any( (i-a in abundant) for a in abundant):
        total += i

total = sum(numbers - pairs)
elapsed = time.time() - start
print "found %s in %s seconds" % (total, elapsed)
