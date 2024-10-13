""" D&C is not an algorithm but a strategy; below examples illustrate it """


def sum_of_values(arr: list[int] | tuple[int]) -> int:
    """
    Recursive function to sum up values of all items in a list
    
    @param arr: a list or a tuple consisting of integers
    @return: sum of all integers from arr
    """
    # base case
    if len(arr) == 0:
        return 0
    # recursive case
    else:
        # this code works correctly for a list of len = 1 because slicing accepts values out of bounds!!! see readme
        return arr[0] + sum_of_values(arr[1:])


print("Sum of values for an empty list: ", sum_of_values([]))
print("Sum of values for a list with one item: ", sum_of_values([3]))


def sum_of_items(arr: list[int] | tuple[int]) -> int:
    """
    Recursive function to count number of items in an array
    
    @param arr: a list or a tuple consisting of integers
    @return: total number of integers in arr
    """
    # base case
    if len(arr) == 0:
        return 0
    # recursive case
    else:
        # it returns 1 to account for arr[0]
        return 1 + sum_of_items(arr[1:])


print("Sum of items for a multiple item list:", sum_of_items([2, 5, 7, 9]))
print("Sum of items for an empty list:", sum_of_items([]))


def find_highest_number(arr: list[int] | tuple[int]) -> int:
    """
    Recursive function to find the highest number in an array
    
    @param arr: a list or a tuple consisting of integers
    @return: the highest integers out of all in arr
    """
    # base case
    if len(arr) == 0:
        return 0
    # another base case
    elif len(arr) == 1:
        return arr[0]
    # recursive case
    else:
        # execution of this code is using call stack mechanism, use debug function to visualize mechanism
        fhn = find_highest_number(arr[1:])
        if arr[0] > fhn:
            return arr[0]
        else:
            return fhn


print(find_highest_number([8, 4, 3, 1, 90]))
print(find_highest_number([91, 8, 4, 3, 1, 90]))
print(find_highest_number([8, 4, 31, 1]))
print(find_highest_number([6]))
print(find_highest_number([]))

def recursive_binary_search(arr, searched_item) -> int:
    """
    It is supposed to find an index of the searched item.
    """
    # base case
    if len(arr) == 0:
        return 0
    # another base case
    elif len(arr) == 1:
        return arr[0]
    else:
        low = 0
        high = len(arr)
        mid = (low + high) // 2
        guessed_item = arr[mid]
        