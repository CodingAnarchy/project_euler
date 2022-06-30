module Collatz
  @@cache = []

  class << self
    def collatz_sequence_length(start)
      return @@cache[start] if @@cache[start]

      chain_length = 1
      current_value = start

      while 1 != current_value
        unless @@cache[current_value].nil?
          chain_length += @@cache[current_value]
          break
        end

        chain_length += 1

        current_value = current_value.even? ? current_value / 2 : (current_value * 3) + 1
      end

      @@cache[start] = chain_length
      chain_length
    end

    def longest_collatz_sequence(limit: 1_000_000)
      (2..limit).max{ |a, b| collatz_sequence_length(a) <=> collatz_sequence_length(b) }
    end
  end
end
