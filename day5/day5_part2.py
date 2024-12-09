# put the rules in an array of tuples

# go through lists line by line and check each element to ensure that each rule is followed

import math

 

incorrectly_ordered = []

ordered = []

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

                    incorrectly_ordered.append(pages_list[i])

            except ValueError:

                # if either page is not found skip this list

                continue

 

def check_if_list_unordered(lst):

    for pages in lst:

        # loop through rules, one at a time

        for first_page, second_page in rules:

            # check each list that the indexof the first is less than the index of the second

            try:

                first_page_index = lst.index(first_page)

                second_page_index = lst.index(second_page)

                if first_page_index > second_page_index:    

                    return True

            except ValueError:

                # if either page is not found skip this list

                continue

    return False

 

def order():

    # need to do

    for pages_list in incorrectly_ordered:

        # while the list is unordered....

        if check_if_list_unordered(pages_list):

            unordered = True

            while (unordered):

                # go through all the rules and if not in order, place the left page one before the right page

                for first_page, second_page in rules:

                    try:

                        first_page_index = pages_list.index(first_page)

                        second_page_index = pages_list.index(second_page)

                        if first_page_index > second_page_index:  

                            # Shift all pages between first_page_index and second_page_index to the left

                            for i in range(second_page_index, first_page_index):

                                pages_list[i] = pages_list[i + 1]

                   

                            # Place the second page to the right of the first page

                            pages_list[first_page_index] = second_page

                    except ValueError:

                        # if either page is not found skip this list

                        continue

                if not check_if_list_unordered(pages_list):

                    unordered = False

                    ordered.append(pages_list)

 

def get_sum_middle_nums():

    sum = 0

    remove_bad_pages()

    # do ordering

    order()

    # get sum

    for pages in ordered:

        print(pages)

        if len(pages) > 0:

            sum += pages[math.floor(len(pages)/2)]

    return sum

 

print(get_sum_middle_nums())