def lengthOfLongestSubstring(s):
    my_letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                  "u", "v", "w", "x", "y", "z"]
    count = 0
    for letter in s:
        if letter in my_letters:
            count += 1
            my_letters.remove(letter)
    return count


print(lengthOfLongestSubstring("abcabcbb"))
