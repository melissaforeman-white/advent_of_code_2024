# when logging a diagonal log the 'a' index
# put this in a dictionary
# if there is already a coordinate in the dictionary then increment num_occurences

word_search = []
a_coordinates = {}
num_occurences = 0
diagonals = ['top-right', 'bottom-right', 'top-left', 'bottom-left']
# Read the file and put into word search array
with open('input.txt', 'r') as file:
    for line in file:
        word_search.append(line[:-1])

def check_coordinates(a_coordinate):
    global num_occurences
    if a_coordinate in a_coordinates:
        print(a_coordinate)
        num_occurences += 1
    else:
        a_coordinates[a_coordinate] = 1

def check_engine(x, y, direction):
    global num_occurences
    i = 1
    word = "M"
    while (i < 3):
        if direction == 'top-right':
            word += word_search[x-i][y+i]
        elif direction == 'top-left':
            word += word_search[x-i][y-i]
        elif direction == 'bottom-right':
            word += word_search[x+i][y+i]
        elif direction == 'bottom-left':
            word += word_search[x+i][y-i]
        i+=1
    if word == "MAS" and direction in diagonals:
        a_coordinate = ()
        if direction == 'top-left':
            a_coordinate = (x-1, y-1)
        elif direction == 'top-right':
            a_coordinate = (x-1, y+1)
        elif direction == 'bottom-right':
            a_coordinate = (x+1, y+1)
        elif direction == 'bottom-left':
            a_coordinate = (x+1, y-1)

        check_coordinates(a_coordinate)

def top_in_bounds(row):
    return row > 1
def bottom_in_bounds(row):
    return row < len(word_search) - 2
def left_in_bounds(col):
    return col > 1
def right_in_bounds(col):
    return col < len(word_search) - 2

def search_for_valid_x():
    # loop over the word search looking for 'x'
    for x, row in enumerate(word_search):
        for y, letter in enumerate(row):
            # letter X found
            if letter == 'M':
                # all in bounds with no edge cases
                if top_in_bounds(x) and bottom_in_bounds(x) and left_in_bounds(y) and right_in_bounds(y):
                    check_engine(x, y, 'top-left')
                    check_engine(x, y, 'top-right')
                    check_engine(x, y, 'bottom-left')
                    check_engine(x, y, 'bottom-right')
                # edge cases exist
                else:
                    # top edge case -> search bottom
                    if not top_in_bounds(x):
                        if not left_in_bounds(y):
                            check_engine(x, y, 'bottom-right')
                        elif not right_in_bounds(y):
                            check_engine(x, y, 'bottom-left')
                        else:
                            check_engine(x, y, 'bottom-right')
                            check_engine(x, y, 'bottom-left')
                    # bottom edge case -> search up
                    elif not bottom_in_bounds(x):
                        if not left_in_bounds(y):
                            check_engine(x, y, 'top-right')
                        elif not right_in_bounds(y):
                            check_engine(x, y, 'top-left')
                        else:
                            check_engine(x, y, 'top-right')
                            check_engine(x, y, 'top-left')
                    # left edge case -> search right
                    elif not left_in_bounds(y):
                        check_engine(x, y, 'top-right')
                        check_engine(x, y, 'bottom-right')
                    # right edge case -> search left
                    elif not right_in_bounds(y):
                        check_engine(x, y, 'top-left')
                        check_engine(x, y, 'bottom-left')

    print(num_occurences)

search_for_valid_x()

