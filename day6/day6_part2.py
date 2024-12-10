# loop over every position in the warehouse and add a blockade #
# then go through the while loop adding each coordinate and appending directions
# if the coordinate and direction is there break out of the loop


warehouse = []
infinite_count = 0
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
    distinct_positions = {}
    guard_direction = 'up'
    guard_location = get_guard_location()
    distinct_positions[guard_location] = ['up']
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
            distinct_positions[guard_location] = [guard_direction]
        elif guard_location in distinct_positions and guard_direction in distinct_positions[guard_location]:
            return False
        else:
            distinct_positions[guard_location].append(guard_direction)
    return True

def add_blockades():
    global infinite_count  # Ensure infinite_count is accessible
    for i, row in enumerate(warehouse):
        row_list = list(row)  # Convert the row to a list of characters
        for j, col in enumerate(row):
            if col == '.':
                row_list[j] = '#'  # Modify the character
                warehouse[i] = ''.join(row_list)  # Convert back to string and update the row
                if not move_guard():
                    infinite_count += 1
                row_list[j] = '.'  # Revert the character
                warehouse[i] = ''.join(row_list)  # Convert back to string and update the row
    print(infinite_count)

add_blockades()

               

 

 

