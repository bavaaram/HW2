#! /usr/bin/python3

def binary_search(case: int, *array: (int, float), lbound=None: (int, float), hbound=None: (int, float)) -> (int, float):
    """
    This function take the case that we want to find it's index,
    list of sorted numbers, and a lower and a upper bound.
    this function work with Binary search Algorithm.
    """
    if lbound == None and hbound == None:
        lbound, hbound = 0, len(array) - 1
    mid = int((lbound + hbound) / 2)
    if array[mid] == case:
        return mid
    elif array[mid] < case:
        return binary_search(case, *array, lbound=mid + 1, hbound=hbound)
    else:
        return binary_search(case, *array, lbound=lbound, hbound=mid - 1)
    
print(binary_search(5, 1, 2, 3, 5, 7, 9, 11, 13))
