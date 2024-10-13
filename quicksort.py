""" Python implementation of quicksort algorithm; one of the fastest sorting algorithms (which also uses D&C) """


def quicksort(array: list | tuple) -> list | tuple:
    """ 
    Implementation from Stack Overflow 
    
    @param array: an unordered array
    @return: an ordered array
    """
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # + joins lists
        return quicksort(less) + equal + quicksort(greater)
    else:
        return array


def quicksort_from_the_book(array: list | tuple) -> list | tuple:
    """ 
    Implementation from the book 
    
    @param array: an unordered array
    @return: an ordered array
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort_from_the_book(less) + [pivot] + quicksort_from_the_book(greater)
