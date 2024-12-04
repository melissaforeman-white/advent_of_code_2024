word_search = []
num_occurences = 0

# Read the file and put into word search array
with open('input.txt', 'r') as file:
    for line in file:
        word_search.append(line[:-1])

def check_engine(x, y, direction):
    global num_occurences
    i = 1
    word = "X"

    while (i < 4):
        if direction == 'left':
            word += word_search[x][y-i]
        elif direction == 'right':
            word += word_search[x][y+i]
        elif direction == 'top':
            word += word_search[x-i][y]
        elif direction == 'bottom':
            word += word_search[x+i][y]
        elif direction == 'top-right':
            word += word_search[x-i][y+i]
        elif direction == 'top-left':
            word += word_search[x-i][y-i]
        elif direction == 'bottom-right':
            word += word_search[x+i][y+i]
        elif direction == 'bottom-left':
            word += word_search[x+i][y-i]
        i+=1
    if word == "XMAS":
        num_occurences += 1

def top_in_bounds(row):
    return row > 2
def bottom_in_bounds(row):
    return row < len(word_search) - 3
def left_in_bounds(col):
    return col > 2
def right_in_bounds(col):
    return col < len(word_search) - 3

def search_for_valid_x():
    # loop over the word search looking for 'x'
    for x, row in enumerate(word_search):
        for y, letter in enumerate(row):
            # letter X found
            if letter == 'X':
                # all in bounds with no edge cases
                if top_in_bounds(x) and bottom_in_bounds(x) and left_in_bounds(y) and right_in_bounds(y):
                    check_engine(x, y, 'top')
                    check_engine(x, y, 'top-left')
                    check_engine(x, y, 'top-right')
                    check_engine(x, y, 'bottom')
                    check_engine(x, y, 'bottom-left')
                    check_engine(x, y, 'bottom-right')
                    check_engine(x, y, 'left')
                    check_engine(x, y, 'right')
                # edge cases exist
                else:
                    # top edge case -> search bottom
                    if not top_in_bounds(x):
                        check_engine(x, y, 'bottom')
                        if not left_in_bounds(y):
                            check_engine(x, y, 'bottom-right')
                            check_engine(x, y, 'right')
                        elif not right_in_bounds(y):
                            check_engine(x, y, 'bottom-left')
                            check_engine(x, y, 'left')
                        else:
                            check_engine(x, y, 'bottom-right')
                            check_engine(x, y, 'bottom-left')
                            check_engine(x, y, 'left')
                            check_engine(x, y, 'right')
                    # bottom edge case -> search up
                    elif not bottom_in_bounds(x):
                        check_engine(x, y, 'top')
                        if not left_in_bounds(y):
                            check_engine(x, y, 'top-right')
                            check_engine(x, y, 'right')
                        elif not right_in_bounds(y):
                            check_engine(x, y, 'top-left')
                            check_engine(x, y, 'left')
                        else:
                            check_engine(x, y, 'top-right')
                            check_engine(x, y, 'top-left')
                            check_engine(x, y, 'left')
                            check_engine(x, y, 'right')
                    # left edge case -> search right
                    elif not left_in_bounds(y):
                        check_engine(x, y, 'top')
                        check_engine(x, y, 'bottom')
                        check_engine(x, y, 'top-right')
                        check_engine(x, y, 'bottom-right')
                        check_engine(x, y, 'right')
                    # right edge case -> search left
                    elif not right_in_bounds(y):
                        check_engine(x, y, 'top')
                        check_engine(x, y, 'bottom')
                        check_engine(x, y, 'top-left')
                        check_engine(x, y, 'bottom-left')
                        check_engine(x, y, 'left')

    print(num_occurences)

search_for_valid_x()

