# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(left, right):
    elements = len(left) + len(right)
    merged_arr = [0] * elements

    curr_index = 0
    while len(left) != 0 and len(right) != 0:
        if left[0] <= right[0]:
            merged_arr[curr_index] = left[0]
            left = left[1:]
            curr_index += 1
        else:
            merged_arr[curr_index] = right[0]
            right = right[1:]
            curr_index += 1

    while len(left) != 0:
        merged_arr[curr_index] = left[0]
        left = left[1:]
        curr_index += 1
    while len(right) != 0:
        merged_arr[curr_index] = right[0]
        right = right[1:]
        curr_index += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    left = arr[:len(arr)//2]
    right = arr[len(arr)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
