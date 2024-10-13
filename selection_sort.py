""" Python implementation of selection sort algorithm """


def find_index_of_lowest_number(arr: list | tuple) -> int:
    """
    Takes 1st item from the list and compares it against all other items to establish the lowest number

    @param arr: an unordered array
    @return: an index of the lowest number from arr
    """

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
    """
    Selection sort is a sorting algorithm, so the array is assumed to be unordered.
    It returns a sorted array.
    It takes O(n^2) time.

    @param arr: an unordered array
    @return: an ordered array
    """
    sorted_arr = []
    arr_copy = list(arr)
    for i in range(len(arr_copy)):
        index_of_lowest_number = find_index_of_lowest_number(arr_copy)
        # this line removes (pops) the lowest number from arr_copy based on its index and appends it to sorted_arr
        sorted_arr.append(arr_copy.pop(index_of_lowest_number))
    return sorted_arr


print(selection_sort([8, 2, 6, 12, 10]))
