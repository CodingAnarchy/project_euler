# The sum of the squares of the first ten natural numbers is:
# 1^2 + 2^2 + ... + 10^2 = 385

# The square of the sum of the first ten natural numbers is:
# (1 + 2 + ... + 10)^2 = 55^2 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and
# the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers

def squared_sum(n)
  ((n + 1) * n / 2) ** 2
end

def sum_squares(n)
  (2 * n + 1) * (n + 1) * n / 6
end

puts squared_sum(100) - sum_squares(100)
