def primes_sieve(lim):
    a = [True] * lim
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i * i, lim, i):
                a[n] = False
