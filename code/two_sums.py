def countOdds(low, high):
    count_odd = 0
    my_list = []
    my_count = 1
    second_count = 2
    if low % 2 == 0:
        for odds in range(low, high + my_count):
            if odds % 2 != 0:
                count_odd += 1
                my_list.append(odds)
    else:
        for odds in range(low, high + second_count):
            if odds % 2 != 0:
                count_odd += 1

    return count_odd


def twoSum(nums, target):
    empty = []
    for number in range(len(nums)):
        for second_number in range(number + 1, len(nums)):
            if nums[number] + nums[second_number] == target:
                empty.append(number)
                empty.append(second_number)
                break
    return empty


print(countOdds(8, 17))
print(twoSum([1, 5, 7, 3, 1, 8], 8  ))
