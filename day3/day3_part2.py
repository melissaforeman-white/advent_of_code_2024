# find enabled
# match for do() and don't()
# if do() add those mul() in the array
# else don't add anything to the array

import re
enabled = True
sum = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"
num_pattern = r'mul\((\d{1,3}),(\d{1,3})\)'

# Read the file
with open('input.txt', 'r') as file:
    file_contents = file.read()
    matches = [match.group() for match in re.finditer(pattern, file_contents)]
    print(matches)

    # Convert matches to integers and decide whether to multiply and add

    for match in matches:
        if match == 'do()':
            enabled = True
        elif match == "don't()":
            enabled = False
        else:
            if enabled:
                nums = re.search(num_pattern, match)
                print(nums)
                num1, num2 = map(int, nums.groups())
                print(num1, num2)
                sum += num1 * num2

    print(sum)

 