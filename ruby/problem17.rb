# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to 1000 (one thousand) inclusive were written out
# in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20
# letters. The use of "and" when writing out numbers is in compliance with
# British usage.

S = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
D = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
H = 7
T = 8

sum = (1..1000).sum do |i|
  c = i % 10  # singles digit
  b = ((i % 100) - c) / 10  # tens digit
  a = ((i % 1000) - (b * 10) - c) / 100  # hundreds digit
  d = ((i % 10000) - (a * 100) - (b * 10) - c) / 1000 # thousands digit

  num_count = 0
  if a != 0 # > 100
    num_count += S[a] + H # e.g. four hundred
    if b != 0 || c != 0
      num_count += 3 # "and"
    end
  end

  if [0, 1].include?(b)
    num_count += S[b * 10 + c]
  else
    num_count += D[b] + S[c]
  end

  if d != 0
    num_count += S[1] + T
  end

  num_count
end

puts sum
