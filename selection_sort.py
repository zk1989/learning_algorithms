"""Python implementation of selection sort algorithm"""


def find_index_of_lowest_number(arr: list | tuple) -> int:
    """Takes first item from the list and compares it against all other items to establish the lowest number"""

    # value arr[0] serves only as a starting point to have something to compare other items to
    temporary_lowest_number = arr[0]
    index_of_lowest_number = 0
    for item in range(1, len(arr)):
        # check if any next item from arr is lower than initial temporary_lowest_number; if yes - overwrite it
        if arr[item] < temporary_lowest_number:
            temporary_lowest_number = arr[item]
            index_of_lowest_number = item
    return index_of_lowest_number


def selection_sort(arr: list | tuple) -> list | tuple:
    new_arr = []
    copied_arr = list(arr)
    for i in range(len(copied_arr)):
        index_of_lowest_number = find_index_of_lowest_number(copied_arr)
        # this line removes the lowest number from copied_arr based on its index and appends it to new_arr
        new_arr.append(copied_arr.pop(index_of_lowest_number))
    return new_arr


print(selection_sort([8, 2, 6, 12, 10]))
