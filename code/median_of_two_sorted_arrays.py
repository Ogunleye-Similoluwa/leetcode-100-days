def findMedianSortedArrays(nums1, nums2):
    another_list = (nums1 + nums2)
    for item in range(len(another_list) - 1):
        for num in range(0, len(another_list) - item - 1):
            if another_list[num] > another_list[num + 1]:
                another_list[num], another_list[num + 1] = another_list[num + 1], another_list[num]
    my_list = another_list[:]
    if len(my_list) % 2 != 0:
        middle = len(my_list) // 2
        return my_list[middle]
    else:
        middle = len(my_list) // 2
        num = (my_list[middle] + my_list[middle - 1]) / 2
        return num


print(findMedianSortedArrays([1, 3], [2, 4]))

