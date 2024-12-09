warehouse = []

# Read the file and put into array of strings
with open('input.txt', 'r') as file:
    for line in file:
        warehouse.append(line[:-1])

def get_guard_location():
    for i, row in enumerate(warehouse):
        for j, col in enumerate(row):
            if col == '^':
                return (i, j)


def rotate_guard_90_degrees(direction):
    # check current direction
    # if current direction is up, move right
    if direction == 'up':
        return 'right'
    # if current direction is right, move down
    elif direction == 'right':
        return 'down'
    # if current direction is down, move left
    elif direction == 'down':
        return 'left'
    # if current direction is left, move up
    elif direction == 'left':
        return 'up'

def move_guard():
    distinct_positions = set()
    guard_direction = 'up'
    guard_location = get_guard_location()
    distinct_positions.add(guard_location)
    boundaries = [0, len(warehouse)-1]
    # while the guard location is not on the outer boundary row = 0 or length - 1 or col = 0 or col = length - 1
    while guard_location[0] not in boundaries and guard_location[1] not in boundaries:
        # move in the current direction until a # is found
        # if direction is up, decrement guard_location[0]
        if guard_direction == 'up':
            if warehouse[guard_location[0] - 1][guard_location[1]] == '#':
                guard_direction = rotate_guard_90_degrees(guard_direction)
            else:
                guard_location = (guard_location[0] - 1, guard_location[1])
        # if direction is right, increment guard_location[1]
        elif guard_direction == 'right':
            if warehouse[guard_location[0]][guard_location[1] + 1] == '#':
                guard_direction = rotate_guard_90_degrees(guard_direction)
            else:
                guard_location = (guard_location[0], guard_location[1] + 1)
        # if direction is down, increment guard_location[0]
        elif guard_direction == 'down':
            if warehouse[guard_location[0] + 1][guard_location[1]] == '#':
                guard_direction = rotate_guard_90_degrees(guard_direction)
            else:
                guard_location = (guard_location[0] + 1, guard_location[1])
        # if direction is left, decrement guard_location[1]
        elif guard_direction == 'left':
            if (guard_location[1] - 1 >= 0):
                if warehouse[guard_location[0]][guard_location[1] - 1] == '#':
                    guard_direction = rotate_guard_90_degrees(guard_direction)
                else:
                    guard_location = (guard_location[0], guard_location[1] - 1)        
        if guard_location not in distinct_positions:
            distinct_positions.add(guard_location)
    
    print(len(distinct_positions))

move_guard()

