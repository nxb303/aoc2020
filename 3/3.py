filename = 'input.txt'
tree = '#'
snow = '.'

# read the dimensions
width = len(open(filename).readline().rstrip('\n'))
height = len(open(filename).readlines())
# initialize the map
map_of_trees = [[0 for x in range(width)] for y in range(height)]
steps_right, steps_down = 3, 1

# initialize the map with values from input
with open(filename) as file:
    x_index = 0
    y_index = 0
    for line in file:
        x_index = 0
        for x in range(width):
            map_of_trees[y_index][x_index] = line[x]
            x_index += 1
        y_index += 1


def encountered_trees(right, down):
    trees = 0
    x_pos, y_pos = 0, 0
    while y_pos < height:
        x_pos += right
        x_pos %= width
        y_pos += down

        if y_pos < height and map_of_trees[y_pos][x_pos] == tree:
            trees += 1

    return trees


print(f"Solution Part 1: {encountered_trees(3, 1)}")

solution_part_two = encountered_trees(1, 1) * encountered_trees(3, 1) * encountered_trees(5, 1) *\
                    encountered_trees(7, 1) * encountered_trees(1, 2)

print(f"Solution Part 2: {solution_part_two}")
