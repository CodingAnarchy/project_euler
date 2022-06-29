import time
from itertools import permutations

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

start = time.time()
for idx, case in enumerate(permutations(digits)):
    if idx == 999999:
        print "Found %s in %s seconds" % (''.join(case), time.time() - start)
        break

