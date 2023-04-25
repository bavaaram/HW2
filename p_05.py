#! /usr/bin/python3

def binary_search(case, *array, lbound=None, hbound=None):
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
