# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_mults(n, k)
  n = (n - 1) / k
  return k * n * (n + 1) / 2
end

def find_sum(n, factors)
  total = factors.reduce(0) { |sum, factor| sum + sum_mults(n, factor) }

  return total - sum_mults(n, factors[0..1].reduce(:*)) 
end

puts find_sum(1000, [3, 5])
