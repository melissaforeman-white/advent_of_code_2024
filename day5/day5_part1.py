# put the rules in an array of tuples
# go through lists line by line and check each element to ensure that each rule is followed

import math

rules = []
pages_list = []

# Clean the data

with open('input.txt', 'r') as file:
    content = file.read()
    parts = content.split('\n\n')
    # Convert each string in the list to a tuple
    rules = [tuple(map(int, item.split('|'))) for item in parts[0].split('\n')[:-1]]
    # Convert each string into an array of strings separated by commas
    pages_list = [page_list.split(',') for page_list in parts[1].split('\n')]
    # Convert the strings to integers
    pages_list = [[int(item) for item in page_list] for page_list in pages_list]

def remove_bad_pages():
    for i, pages in enumerate(pages_list):
        # loop through rules, one at a time
        for first_page, second_page in rules:
            # check each list that the indexof the first is less than the index of the second
            try:
                first_page_index = pages.index(first_page)
                second_page_index = pages.index(second_page)
                if first_page_index > second_page_index:    
                    pages_list[i] = []
            except ValueError:
                # if either page is not found skip this list
                continue

def get_sum_middle_nums():
    sum = 0
    remove_bad_pages()
    for pages in pages_list:
        if len(pages) > 0:
            print(pages[math.floor(len(pages)/2)])
            sum += pages[math.floor(len(pages)/2)]
    return sum

print(get_sum_middle_nums())