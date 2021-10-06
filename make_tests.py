from main import selection_sort, insertion_sort, merge_sort, shell_sort, merge_counter
import random
import json
import time


def first(length):
    possible_vars = []
    comparison = {"insertion sort": 0, "selection sort": 0,
                  "merge sort": 0, "shell sort": 0}
    time_dict = {"insertion sort": 0, "selection sort": 0,
                 "merge sort": 0, "shell sort": 0}
    for _ in range(5):
        listt = [random.randint(0, length) for i in range(length)]
        possible_vars.append(listt)
    for array in possible_vars:
        start = time.time()
        res = insertion_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["insertion sort"] += res
        time_dict["insertion sort"] += time1
        start = time.time()
        res = selection_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["selection sort"] += res
        time_dict["selection sort"] += time1
        start = time.time()
        res = merge_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["merge sort"] += res
        merge_counter = 0
        time_dict["merge sort"] += time1
        start = time.time()
        res = shell_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["shell sort"] += res
        time_dict["shell sort"] += time1
    for key in comparison:
        comparison[key] == comparison[key]/5
        time_dict[key] == time_dict[key]/5
    return comparison, time_dict


def second_and_third(array):
    comparison = {"insertion sort": 0, "selection sort": 0,
                  "merge sort": 0, "shell sort": 0}
    time_dict = {"insertion sort": 0, "selection sort": 0,
                 "merge sort": 0, "shell sort": 0}
    # test = Sort(array)
    # array_for_merge = array.copy()
    start = time.time()
    res = insertion_sort(array)[1]
    end = time.time()
    time1 = end - start
    comparison["insertion sort"] += res
    time_dict["insertion sort"] += time1
    start = time.time()
    res = selection_sort(array)[1]
    end = time.time()
    time1 = end - start
    comparison["selection sort"] += res
    time_dict["selection sort"] += time1
    start = time.time()
    res = merge_sort(array)[1]
    end = time.time()
    time1 = end - start
    comparison["merge sort"] += res
    merge_counter = 0
    time_dict["merge sort"] += time1
    start = time.time()
    res = shell_sort(array)[1]
    end = time.time()
    time1 = end - start
    comparison["shell sort"] += res
    time_dict["shell sort"] += time1
    return comparison, time_dict


def fourth(length):
    possible_vars = []
    comparison = {"insertion sort": 0, "selection sort": 0,
                  "merge sort": 0, "shell sort": 0}
    time_dict = {"insertion sort": 0, "selection sort": 0,
                 "merge sort": 0, "shell sort": 0}
    for _ in range(3):
        listt = [random.randint(1, 4) for i in range(length)]
        possible_vars.append(listt)
    for array in possible_vars:
        start = time.time()
        res = insertion_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["insertion sort"] += res
        time_dict["insertion sort"] += time1
        start = time.time()
        res = selection_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["selection sort"] += res
        time_dict["selection sort"] += time1
        start = time.time()
        res = merge_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["merge sort"] += res
        merge_counter = 0
        time_dict["merge sort"] += time1
        start = time.time()
        res = shell_sort(array)[1]
        end = time.time()
        time1 = end - start
        comparison["shell sort"] += res
        time_dict["shell sort"] += time1
    for key in comparison:
        comparison[key] == comparison[key]/3
        time_dict[key] == time_dict[key]/3
    return comparison, time_dict


if __name__ == '__main__':
    all_comparison = {i: {} for i in range(7, 16)}
    all_time = {i: {} for i in range(7, 16)}
    for poww in range(7, 16):
        length = 2**poww
        res = first(length)
        first_ex = res[0]
        first_ex1 = res[1]
        array = [random.randint(0, length) for i in range(length)]
        res = second_and_third(sorted(array))
        second_ex = res[0]
        second_ex1 = res[1]
        res = second_and_third(sorted(array, reverse=True))
        third_ex = res[0]
        third_ex1 = res[1]
        res = fourth(length)
        fourth_ex = res[0]
        fourth_ex1 = res[1]
        all_comparison[poww] = {"first": first_ex, "second": second_ex,
                                "third": third_ex, "fourth": fourth_ex}
        all_time[poww] = {"first": first_ex1, "second": second_ex1,
                          "third": third_ex1, "fourth": fourth_ex1}

    with open('comparison_test.json', 'w') as fp:
        json.dump(all_comparison, fp)
    with open('time_test.json', 'w') as fp:
        json.dump(all_time, fp)
