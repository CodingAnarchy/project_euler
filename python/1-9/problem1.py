"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_mults(n, k):
  n = int((n - 1) / k)
  return k * n * (n + 1) / 2

def find_sum(n, factors):
  """
  :param n: maximum number to find multiples below
  :param factors: factors to find multiples of (tuple of two)
  :return: sum of multiples of factors below n
  """
  # sum(j or k) = sum(j) + sum(k) - sum(j * k)
  # sum_j(n) = sum(k*i) from i = 1 to i = (n - 1) / k
  # sum(k*i) = k * n * (n + 1) / 2
  total = 0
  for factor in factors:
    total += sum_mults(n, factor)
  return total - sum_mults(n, factors[0] * factors[1])


print(find_sum(1000, (3, 5)))
