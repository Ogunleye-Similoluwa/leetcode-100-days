import sys


def reverse(x):
    total = 0
    if (-2 ** 31) <= x < 0:
        num_str = str(x)
        reversed_str = num_str[:0:-1]
        new_total = int(reversed_str) * -1
        if new_total > (2 ** 31) or new_total < (-2 ** 31):
            return 0
        return new_total
    while (2 ** 31) - 1 > x > 0:
        rem = x % 10
        total = (total * 10) + rem
        x //= 10
        if total > (2 ** 31) or total < (-2 ** 31):
            return 0

    return total


print(reverse(-321))
