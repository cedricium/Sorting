# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        min_idx = smallest_index
        for j in range(i + 1, len(arr)):
            min_idx = j if arr[min_idx] > arr[j] else min_idx
        # TO-DO: swap
        # arr[i], arr[min_idx] = arr[min_idx], arr[i]
        tmp_num = arr[smallest_index]
        arr[smallest_index] = arr[min_idx]
        arr[min_idx] = tmp_num

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    if len(arr) == 0:
        return []
    elif min(arr) < 0:
        return "Error, negative numbers not allowed in Count Sort"

    count = [0] * (max(arr) + 1)  # fill count with (largest num in arr) zeros
    sort = [0] * len(arr)         # fill sort with same length as arr zeros

    # count the number of occurrences of each num in arr
    for i in range(len(arr)):
        count[arr[i]] += 1

    # ???
    total = 0
    for i in range(0, len(count)):
        count[i], total = total, count[i] + total
    # print(count)

    # ???
    for i in range(0, len(arr)):
        idx = count[arr[i]]
        sort[idx] = arr[i]
        count[arr[i]] -= 1
    # print(sort)

    return sort
