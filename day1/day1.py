# sort each list
# take absolute value of the difference of min nums
# add to sum
# remove those mins nums from each list
# continue until list length equals 0

# Initialize arrays
array1 = []
array2 = []

# Initialize sum
sum = 0

# Read the file
with open('/Users/melissaforeman/Documents/Advent of Code 2024/day1/input.txt', 'r') as file:
    for line in file:
        # Split each line into two parts
        values = line.split()
        # Append values to respective arrays
        array1.append(int(values[0]))
        array2.append(int(values[1]))

array1.sort()
array2.sort()

print(array1)
for i in range(len(array1)):
    min1 = array1[i]
    min2 = array2[i]
    sum += abs(min1 - min2)

print("sum ", sum)
