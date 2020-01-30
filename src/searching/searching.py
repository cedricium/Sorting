# STRETCH: implement Linear Search
def linear_search(arr, target):
    for idx, num in enumerate(arr):
        if num == target:
            return idx
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    while (low <= high):
        mid = int((high - low) / 2) + low
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    elif arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary_search_recursive(arr, target, low, middle - 1)
    elif arr[middle] < target:
        return binary_search_recursive(arr, target, middle + 1, high)
    else:
        return -1
