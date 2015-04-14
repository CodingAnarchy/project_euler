from math import sqrt, ceil

def primes_sieve(lim):
    a = [True] * lim
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, lim, i):
                a[n] = False

prime_factors = []
for prime in primes_sieve(int(ceil(sqrt(600851475143)))):
    if 600851475143 % prime == 0:
        prime_factors.append(prime)

print prime_factors