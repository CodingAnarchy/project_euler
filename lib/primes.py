from collections import OrderedDict


def primes_sieve(lim):
    primes = [True] * lim
    primes[0] = primes[1] = False
    for i, isprime in enumerate(primes):
        if isprime:
            primes[i*2::i] = [False] * (((lim - 1) / i) - 1)
            yield i


def fast_nth_prime(n, lim=125000):
    if lim % 2 != 0:
        lim += 1
    primes = [True] * lim
    primes[0] = primes[1] = False
    count = 0  # how many primes have we found?
    for i, isprime in enumerate(primes):
        if isprime:
            # sieve out non-primes by multiples of known primes
            primes[i*2::i] = [False] * (((lim - 1) / i) - 1)
            count += 1
        if count == n:
            return i
    return False


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