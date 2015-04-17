from math import sqrt
from lib.divisors import gcd


def pyth_triplet(s):
    for m in xrange(2, int(sqrt(s / 2))):
        if (s / 2) % m == 0:  # m found
            if m % 2 == 0:  # ensure k is odd
                k = m + 1
            else:
                k = m + 2

            while k < 2 * m and k <= s / (2 * m):
                if s / (2 * m) % k == 0 and gcd(k, m) == 1:
                    d = s / 2 / (k * m)
                    n = k - m
                    a = d * (m * m - n * n)
                    b = 2 * d * m * n
                    c = d * (m * m + n * n)
                    return a, b, c
                k += 2

print pyth_triplet(1000)
