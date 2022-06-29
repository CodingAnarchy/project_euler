# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def max_palindrome(minimum: 100, maximum: 999)
  (minimum...maximum).reverse_each.filter_map do |left|
    (minimum...maximum).reverse_each.filter_map do |right|
      x = (left * right).to_s
      x.to_i if x == x.reverse
    end.max
  end.max
end

puts max_palindrome
