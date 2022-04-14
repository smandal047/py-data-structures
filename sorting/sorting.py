def bubble_sort(arr):
    """

    :param arr:
    :return:
    """
    length = len(arr)

    for step in range(length):

        for index, item in enumerate(arr):

            if index + 1 == length:
                break

            if arr[index] < arr[index + 1]:
                swap(arr, index, index + 1)

    return arr


def improved_bubble_sort(arr):
    """

    :param arr:
    :return:
    """
    length = len(arr)

    for step in range(length - 1):
        sorted = True

        for index in range(length - 1 - step):

            if arr[index] < arr[index + 1]:
                swap(arr, index, index + 1)
                sorted = False

        # we are skipping the whole sorting process if the array is sorted
        if sorted:
            break

    return arr


def selection_sort(arr):
    length = len(arr)

    for step in range(length):
        sliced_array = arr[step:]

        max_holder = sliced_array[0]
        max_index = 0

        # find max item index
        for index, item in enumerate(sliced_array):
            if item > max_holder:
                max_holder = item
                max_index = index

        swap(arr, step, step + max_index)

    return arr


def swap(arr, i1, i2):
    arr[i1], arr[i2] = arr[i2], arr[i1]


def insertion_sort(arr):
    length = len(arr)

    for index in range(1, length - 1):

        # checking for the next item, if its greater swap
        if arr[index] > arr[index + 1]:
            swap(arr, index, index + 1)

            # backtrack all the positions and compare with sorted sub-list
            # if the previous item is greater then swap and repeat
            while arr[index] < arr[index - 1] and index > 0:
                swap(arr, index, index - 1)
                index -= 1

    return arr


def shell_sort(arr):
    length = len(arr)

    interval_size = length // 2

    while interval_size > 0:

        for index in range(1, length - interval_size):

            if arr[index] > arr[index + interval_size]:
                swap(arr, index, index + interval_size)

                while arr[index] < arr[index - interval_size] and index > 0:
                    swap(arr, index, index - interval_size)
                    index -= 1

        interval_size //= 2

    return arr


def two_way_merge(a1, a2):
    a1_min_pt = 0
    a2_min_pt = 0
    sorted_arr = []
    for i in range(len(a1) + len(a2)):

        if a1[a1_min_pt] < a2[a2_min_pt]:
            sorted_arr.append(a1[a1_min_pt])
            a1_min_pt += 1
        else:
            sorted_arr.append(a2[a2_min_pt])
            a2_min_pt += 1

        if a1_min_pt >= len(a1):
            [sorted_arr.append(i) for i in a2[a2_min_pt:]]
            break
        if a2_min_pt >= len(a2):
            [sorted_arr.append(i) for i in a1[a1_min_pt:]]
            break

    return sorted_arr


def merge_sort(arr):

    if len(arr) > 1:

        # divide the array
        mid = len(arr) // 2
        l = arr[:mid]
        h = arr[mid:]

        # Sort the two halves
        a1 = merge_sort(l)
        a2 = merge_sort(h)

        return two_way_merge(a1, a2)

    else:
        return arr


if __name__ == '__main__':
    a = [5, 8, 6, 4, 0, 9, 1]
    b = [7, 10, 2, 14, 11, 13, 12]

    # import random
    # a = [random.randint(100, 10000) for i in range(10000)]

    print('--=sorted truth=--')
    print(sorted(a))
    print('------------------')

    print(bubble_sort(a))

    print(improved_bubble_sort(a))

    print(selection_sort(a))

    print(insertion_sort(a))

    print(shell_sort(a))

    # print(two_way_merge(sorted(a), sorted(b)))

    print(merge_sort(a))
