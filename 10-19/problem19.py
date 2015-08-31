import time
from datetime import date, timedelta

start = time.time()
# initial start date given - Jan 1 1901
sundays = 0
d = date(1901, 1, 1)
if d.weekday() == 6:
    sundays += 1
d += timedelta(days=6 - d.weekday())
while d.year <= 2000:
    if d.day == 1:
        sundays += 1
    d += timedelta(days=7)

elapsed = (time.time() - start)
print "%s Sundays fell on the first of the month in the 20th century, \
       found in %s" % (sundays, elapsed)
