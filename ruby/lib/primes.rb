require 'set'

module Primes
  class << self
    def sieve(lim)
      raise ArgumentError.new("Limit of the prime sieve must be >= 2.") unless lim >= 2

      Enumerator.new do |y|
        non_primes = Set.new
        (2..lim).each do |val|
          if !non_primes.include?(val)
            (2..(lim/val)).each { |x| non_primes << x * val }
            y << val
          end
        end
      end
    end

    def fast_nth(n, lim: 125_000)
      lim += 1 if lim % 2 != 0

      sieve(lim).take(n)[-1]
    end

    def multiplicity(n)
      raise ArgumentError.new("Too much memory will be consumed; use lower n") if n > 100_000

      primes = sieve(n).to_h { |i| [i, 1] }
      (4..(n + 1)).each do |i|
        primes.each do |p, v|
          x = 0
          while i % p == 0
            x += 1
            i /= p
          end
          primes[p] = [v, x].max
        end
      end

      primes
    end
  end
end
