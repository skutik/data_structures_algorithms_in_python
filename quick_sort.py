"""Implement quick sort in Python.
Input a list.
Output a sorted list.
https://classroom.udacity.com/courses/ud513/lessons/7123524086/concepts/78868166210923
"""

def quicksort(array):
    if len(array) > 1:
        pivot_to_check = [[0,len(array) - 1]]
        while pivot_to_check:
            pivot = pivot_to_check[0][1]
            current_target = pivot_to_check[0][0]
            while current_target != pivot:
                print "A: {0}, P: {1}, CV: {2}".format(array, array[pivot], array[current_target])
                if array[current_target] > array[pivot]:
                    if pivot - current_target > 1:
                        array[pivot], array[pivot - 1], array[current_target] = array[current_target], array[pivot], array[pivot - 1]
                    else:
                        array[pivot], array[current_target] = array[current_target], array[pivot]
                    pivot -= 1
                elif array[current_target] <= array[pivot]:
                    current_target += 1
            if array[pivot + 1] < array[pivot]:
                array[pivot + 1], array[pivot] = array[pivot], array[pivot + 1]
            if pivot_to_check[0][1] - pivot_to_check[0][0] > 1:
                upper_bound = pivot + 1
                lower_bound = pivot - 1
                if pivot_to_check[0][0] < lower_bound:
                    pivot_to_check.append([pivot_to_check[0][0], lower_bound])
                if upper_bound < pivot_to_check[0][1]:
                    pivot_to_check.append([upper_bound, pivot_to_check[0][1]])
            del pivot_to_check[0]
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)