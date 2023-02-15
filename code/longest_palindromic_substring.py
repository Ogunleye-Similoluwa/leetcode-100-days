def longestPalindrome(s):
    my_list = []
    my_second_list = []
    append_letters = ""
    for i in s:
        my_list.append(i)

    for item in range(0, len(my_list) - 1):
        for letter in range(1, len(my_list)):
            if my_list[item] in my_list[1:]:
                append_letters += my_list[letter]
                if my_list[item] == my_list[letter]:
                    append_letters += my_list[item]
                    return append_letters


print(longestPalindrome("babad"))
