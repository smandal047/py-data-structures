def binary_search(nums, target):

    length = len(nums)
    half_length = (length // 2)
    index = 0

    if length == 1 and target == nums[0]:
        return 0
    elif length == 1 and target != nums[0]:
        return 'string'


    # 'case 1'
    if target == nums[half_length]:
        index += half_length
        return index

    # 'case 2'
    elif target < nums[half_length]:
        index -= binary_search(nums[:half_length], target)
        return index

    # 'case 3'
    elif target > nums[half_length]:
        index += binary_search(nums[half_length + 1:], target)
        return index


if __name__ == '__main__':

    nums = [2, 5, 6, 8, 9, 10]
    target = 9

    index = binary_search(nums, target)
    print(index)
    if index:
        print('Element found at index', index)
    else:
        print('Element found not in the list')
