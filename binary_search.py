"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list.
https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/78812066010923
"""
from time import sleep

def binary_search(input_array, value):
    length = len(input_array) - 1
    search_index = length/2
    lower_index = 0
    upper_index = length
    while True:
        current_value = input_array[search_index]
        if value == current_value:
            return search_index
        elif upper_index == lower_index:
            return - 1
        elif value > current_value:
            lower_index = search_index + 1
            search_index = (upper_index + search_index +1)/2
        elif value < current_value:
            upper_index = search_index
            search_index = (search_index - 1)/2

test_list = [1,3,9,11,15,19,25,29]
test_val1 = 2
test_val2 = 25
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)