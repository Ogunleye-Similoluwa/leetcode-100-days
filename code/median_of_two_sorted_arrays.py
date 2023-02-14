def findMedianSortedArrays(nums1, nums2):
    another_list = (nums1 + nums2)
    for item in range(len(another_list) - 1):
        for num in range(0, len(another_list) - item - 1):
            if another_list[num] > another_list[num + 1]:
                another_list[num], another_list[num + 1] = another_list[num + 1], another_list[num]
    print(another_list)
    for i in range(0, len(another_list) - 1):
        if len(another_list) % 2 != 0:
            middle = len(another_list) // 2
            return float(another_list[middle])
        else:
            middle = (len(another_list) - 1) // 2
            double_middle = float((another_list[middle] + another_list[middle + 1]) / 2)
            return double_middle, another_list[middle], another_list[middle + 1]
    return another_list


print(findMedianSortedArrays([1, 5], [6, 4]))
