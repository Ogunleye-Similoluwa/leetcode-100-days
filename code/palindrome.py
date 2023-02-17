def isPalindrome(x):
    total = 0
    my_num = x
    while 0 <= x <= 2 ** 31 - 1:
        rem = x % 10
        total = (total * 10) + rem
        x //= 10
        if total == my_num:
            return True
        elif x == 0:
            return False


print(isPalindrome(10))
