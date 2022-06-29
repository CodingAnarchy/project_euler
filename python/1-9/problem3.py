from math import sqrt, ceil
from lib.primes import primes_sieve

prime_factors = []
for prime in primes_sieve(int(ceil(sqrt(600851475143)))):
    if 600851475143 % prime == 0:
        prime_factors.append(prime)

print(prime_factors)
