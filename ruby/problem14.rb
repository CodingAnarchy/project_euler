require_relative 'lib/collatz'

puts Collatz.longest_collatz_sequence(limit: 1_000_000)
