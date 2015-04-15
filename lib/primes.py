from collections import OrderedDict

def primes_sieve(lim):
    a = [True] * lim
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, lim, i):
                a[n] = False


def multiplicity(n):
    # Creating list of primes - ensure lower n to limit memory usage
    if n > 100000:
        raise RuntimeError("Use smaller number to prevent memory error")
    primes = OrderedDict(zip(list(primes_sieve(n)), [1] * n))
    for n in xrange(4, n + 1):
        for prime in primes:
            i = 0
            while n % prime == 0:
                i += 1
                n /= prime
                if i > primes[prime]:
                    primes[prime] = i
    return primes