module MathUtils
  class << self
    def prod(enumerable)
      enumerable.reduce(:*)
    end

    def factorial(n)
      prod(1...n)
    end

    def sum_digits(n)
      n.to_s.reduce(0) { |total, digit| total += digit.to_i }
    end
  end
end
