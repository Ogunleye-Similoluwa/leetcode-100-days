def find_longest(palindrome_list):
    max_length = 0
    longest_pal = ''
    for palindrome in palindrome_list:
        if len(palindrome) > max_length:
            longest_pal = palindrome
    return longest_pal


def longestPalindrome(s):
    my_list = []
    my_second_list = []
    append_letters = ""
    for i in s:
        my_list.append(i)

    second_s = s[::-1]
    pal_list = []
    pal_string = ''
    for i in range(0, len(s)):
        for j in range(0, len(s)):
            if s[i] == second_s[j]:
                pal_string += second_s[j]
            else:
                pal_list.append(pal_string)
                pal_string = ''

    return find_longest(pal_list)

    # for item in range(0, len(my_list) - 1):
    #     for letter in range(1, len(my_list)):
    #         if my_list[item] in my_list[::]:
    #             append_letters += my_list[letter]
    #             if my_list[item] == my_list[letter]:
    #                 append_letters += my_list[item]
    #                 return append_letters


print(longestPalindrome("babad"))
