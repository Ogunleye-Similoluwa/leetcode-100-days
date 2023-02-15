def addTwoNums(list1, list2):
    carry_over = 0
    empty = []
    for i in range(0, len(list1)):
        new_num = list1[i] + list2[i]
        if new_num > 9:
            num = new_num + carry_over
            carry_over = num - 9
            rem = new_num % 2
            if rem == 0:
                empty.append(rem)
        elif carry_over < 0 and carry_over <= 9:
            empty.append(new_num)
        else:
            num = new_num + carry_over
            empty.append(num)
    return empty, carry_over



def merge(nums1, m, nums2, n):
        # """
        # :type nums1: List[int]
        # :type m: int
        # :type nums2: List[int]
        # :type n: int
        # :rtype: void Do not return anything, modify nums1 in-pla
        # ce instead.
        # """
        last1 = m - 1
        last2 = n - 1
        last = m + n - 1
        while last1 >= 0 and last2 >= 0:
            if nums1[last1] > nums2[last2]:
                nums1[last] = nums1[last1]
                last1 -= 1
                last -= 1
            else:
                nums1[last] = nums2[last2]
                last2 -= 1
                last -= 1
        while last2 >= 0:
            nums1[last] = nums2[last2]
            last -= 1
            last2 -= 1


print(addTwoNums([2, 4, 3], [5, 6, 4]))
