"""D&C is not an algorithm but a strategy; the concept is allegedly illustrated by the below examples as per the book"""


def sum_of_values(arr) -> int:
    """Sum up values of all items in a list using recursion"""
    # base case
    if len(arr) == 0:
        return 0
    # recursive case
    else:
        # this code only works correctly for a list of len = 1 because slicing accepts values out of bounds!!!
        return arr[0] + sum_of_values(arr[1:])


# print(sum_of_values([3]))


def sum_of_items(arr: list | tuple) -> int:
    """Recursive function to count number of items in an array"""
    # base case
    if len(arr) == 0:
        return 0
    # recursive case
    else:
        # it returns 1 to count for arr[0]
        return 1 + sum_of_items(arr[1:])


# print(sum_of_items([2, 5, 7, 9]))
# print(sum_of_items([]))

def find_highest_number(arr: list | tuple) -> int:
    """Recursive function to find the highest number in an array"""
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
