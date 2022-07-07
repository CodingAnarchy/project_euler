# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

require_relative '../lib/primes'

def smallest_evenly_divisible(limit)
  mults = Primes.multiplicity(limit)
  mults.reduce(1) do |result, (k, v)|
    result *= k ** v
  end
end

puts smallest_evenly_divisible(20)
