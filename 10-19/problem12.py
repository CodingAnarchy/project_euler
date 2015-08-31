"""


The sequence of triangle numbers is generated by adding the natural numbers.
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over 500 divisors?
"""

import math
import sys

a = 1
b = 2

while True:
    a = a + b
    b += 1
    l = []

    sqrt_a = int(math.sqrt(a))

    for x in range(1, sqrt_a + 1):
        if a % x == 0:
            l.append(x)
            if x < math.sqrt(a):
                l.append(a // x)
            if len(l) > 500:
                print a
                sys.exit(0)
