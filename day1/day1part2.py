# initialize arrays
# initialize a sum
# clean the data and place into arrays
# iterate over left list and count how many times it occurs in the right list
# multiple the number and the # times it occured and add to sum

# Initialize arrays
array1 = []
array2 = []

# Initialize sum
sum = 0

# Read the file and put values into arrays
with open('/Users/melissaforeman/Documents/Advent of Code 2024/day1/input.txt', 'r') as file:
    for line in file:
        # Split each line into two parts
        values = line.split()
        # Append values to respective arrays
        array1.append(int(values[0]))
        array2.append(int(values[1]))


for num in array1:
    count = array2.count(num)
    sum += count * num

print(sum)