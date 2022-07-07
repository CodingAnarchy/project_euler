# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def route_num(grid_size)
  l = Array.new(grid_size, 1)

  (0..l.length).each do |i|
    (1...i).each do |j|
      l[j] += l[j - 1]
    end

    l[i] = 2 * l[i - 1]
  end

  l[grid_size - 1]
end

puts route_num(20)
