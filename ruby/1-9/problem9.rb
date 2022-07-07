# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a ** 2 + b ** 2 = c ** 2
# For example, 3 ** 2 + 4 ** 2 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

require_relative 'lib/math_utils'

def pythagorean_triplets(s)
  (2...Math.sqrt(s / 2).floor).each do |m|
    if (s / 2) % m == 0  # m found
      k = m % 2 == 0 ? m + 1 : m + 2  # ensure k is odd

      while k < 2 * m && k <= s / (2 * m)
        if s / (2 * m) % k == 0 && k.gcd(m) == 1
          d = s / 2 / (k * m)
          n = k - m
          a = d * (m * m - n * n)
          b = 2 * d * m * n
          c = d * (m * m + n * n)
          return a, b, c
        end

        k += 2
      end
    end
  end
end

puts MathUtils.prod(pythagorean_triplets(1000))
