def addBinary(a, b):
    new_num = int(a) + int(b)
    carry_over = 0
    total = 0
    while new_num != 0:
        r = new_num % 10
        if r >= 2:
            rem = r % 2
            carry_over = rem
            total += (total * 10) + rem
            new_num = new_num // 10 + carry_over
        else:
            total += (total * 10) + carry_over
            new_num = new_num // 10

        # new_num = new_num // 10

    return total



print(addBinary("11", "1"))
