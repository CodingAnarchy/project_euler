# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

require_relative "../lib/primes"

def prime_factors(n)
  prime_limit = Math.sqrt(n).ceil
  Primes.sieve(prime_limit).select do |prime|
    n % prime == 0
  end
end


puts prime_factors(600_851_475_143)[-1]
