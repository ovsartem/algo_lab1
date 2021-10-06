import copy
merge_counter = 0


def selection_sort(array):
    arr = copy.deepcopy(array)
    counter = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        counter += 1
    return arr, counter


def insertion_sort(array):
    arr = copy.deepcopy(array)
    counter = 0
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        counter += 1
    return arr, counter


def shell_sort(array):
    arr = copy.deepcopy(array)
    counter = 0
    length = len(arr)
    gap = 1

    if length <= 1:
        return arr, counter
    gap = 1
    while gap < length/3:
        gap = 3*gap+1
    while gap >= 1:
        for index in range(gap, length):
            for ind in range(index, gap-1, -gap):
                counter += 1
                if arr[ind] < arr[ind-gap]:
                    arr[ind], arr[ind -
                                  gap] = arr[ind-gap], arr[ind]
                else:
                    break
        gap //= 3
    return arr, counter


def merge(left, right):
    global merge_counter
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        merge_counter += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def main_merge(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = main_merge(arr[:mid])
        right = main_merge(arr[mid:])
        return merge(left, right)
    else:
        return arr


def merge_sort(arr):
    arr = main_merge(arr)
    return arr, merge_counter
