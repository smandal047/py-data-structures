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
                arr[index], arr[index + 1] = arr[index + 1], arr[index]

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
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
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

        arr[step], arr[step + max_index] = arr[step + max_index], arr[step]

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


if __name__ == '__main__':
    a = [5, 8, 6, 4, 0, 9, 1]

    # import random
    # a = [random.randint(100, 100000) for i in range(10000)]

    print('--=sorted truth=--')
    print(sorted(a))
    print('------------------')

    # print(bubble_sort(a))
    #
    # print(improved_bubble_sort(a))
    #
    # print(selection_sort(a))

    # print(insertion_sort(a))

    print(shell_sort(a))
