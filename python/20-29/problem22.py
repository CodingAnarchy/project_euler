#!/usr/bin/env python
import time

start = time.time()
score_total = 0
with open("p022_names.txt") as names_file:
    names = names_file.read().replace('"', '').split(",")
    names.sort()
    for idx, name in enumerate(names):
        sum_chars = sum([ord(ch) - 96 for ch in name.lower()])
        score = sum_chars * (idx + 1)
        score_total += score

elapsed = time.time() - start
print "found %s in %s seconds" % (score_total, elapsed)
