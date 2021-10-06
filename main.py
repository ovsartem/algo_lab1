import copy


def selection_sort(array):
    """
    selection sort
    """
    arr = copy.deepcopy(array)
    counter = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            counter += 1
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return counter


def insertion_sort(array):
    """
    insertion sort
    """
    arr = copy.deepcopy(array)
    counter = 0
    for i in range(1, len(arr)):

        key = arr[i]
        j = i-1
        counter += 1
        while j >= 0 and key < arr[j]:
            counter += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return counter


def shell_sort(array):
    """
    shell sort
    """
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
    return counter


def merge_sort(array):
    counter = 0
    if len(array) > 1:
        mid = len(array) // 2

        left_array = array[:mid]
        array_right = array[mid:]

        counter = merge_sort(left_array) + merge_sort(array_right)

        left_idx = right_idx = idx = 0

        while left_idx < len(left_array) and right_idx < len(array_right):
            counter += 1
            if left_array[left_idx] < array_right[right_idx]:
                array[idx] = left_array[left_idx]
                left_idx += 1
            else:
                array[idx] = array_right[right_idx]
                right_idx += 1
            idx += 1

        while left_idx < len(left_array):
            array[idx] = left_array[left_idx]
            left_idx += 1
            idx += 1

        while right_idx < len(array_right):
            array[idx] = array_right[right_idx]
            right_idx += 1
            idx += 1

    return counter


