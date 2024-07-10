def binary_search(arr: list|tuple, item: int):
    """ Python implementation of binary search algorithm"""
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = list(range(1, 1461))
my_tuple = tuple(range(1, 1461))

# to-do: check run times for both implementations
print(binary_search(my_list, 5))
print(binary_search(my_tuple, 5))
