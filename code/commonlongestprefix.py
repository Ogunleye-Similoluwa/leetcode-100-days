def longestCommonPrefix(strs):
    letters_append = ""
    count = len(strs) - 1
    second_count = 0
    for letters in strs:
        for letter in letters:
            if letter in strs[count]:
                if len(strs[second_count]) == letter:
                letters_append += letter

        return letters_append

        # print(letter)
    # count -= 1
    # return letters_append


print(longestCommonPrefix(["flower", "flow", "flight"]))
