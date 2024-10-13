""" Python implementation of binary search algorithm and other trivia """

import sys
import timeit


def binary_search(arr: list | tuple, searched_item: int) -> int | None:
    """
    Binary search returns the position (index) of an item in an ordered array.
    It takes O(log n) time ("log time").

    @param arr: an ordered array
    @param searched_item: the item which position (index) we are looking for
    @return: the position (index) of a searched item if it exists in the given array
    """

    # low and high together form a range of indices we are searching through
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guessed_item = arr[mid]
        if guessed_item == searched_item:
            return mid
        elif guessed_item > searched_item:
            high = mid - 1
        else:
            low = mid + 1
    # searched_item doesn't exist in the given array
    return None


my_list = list(range(1, 146100))
my_tuple = tuple(range(1, 146100))

# this illustrates that tuples take less space in memory than lists
print("Memory consumption in bytes for a list: ", sys.getsizeof(my_list))
print("Memory consumption in bytes for a tuple: ", sys.getsizeof(my_tuple))

# this illustrates that tuples are slightly faster in performance than lists
list_start_time = timeit.default_timer()
binary_search(my_list, 789)
list_end_time = timeit.default_timer()
list_elapsed_time = list_end_time - list_start_time
print(f"Runtime of binary search for a list is: {list_elapsed_time}")

tuple_start_time = timeit.default_timer()
binary_search(my_tuple, 53457)
tuple_end_time = timeit.default_timer()
tuple_elapsed_time = tuple_end_time - tuple_start_time
print(f"Runtime of binary search for a tuple is: {tuple_elapsed_time}")

print("Index for searched item 1235 in a list is:", binary_search(my_list, 1235))
print("When searched item is out of range result is:", binary_search(my_list, 654775))
print("Index for searched item 5 in a tuple is:", binary_search(my_tuple, 5))
