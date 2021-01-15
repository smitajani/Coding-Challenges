

def lengthOfLongestSubstring(s: str) -> int:
    """ Returns length of longest substring without any repeating characteers
        >>> lengthOfLongestSubstring("abcabcbb")
        3

        >>> lengthOfLongestSubstring("uqinntq")
        4

        >>> lengthOfLongestSubstring("abba")
        2

        >>> lengthOfLongestSubstring("dvdf")
        3

        >>> lengthOfLongestSubstring("bbbbb")
        1

        >>> lengthOfLongestSubstring("pwwkew")
        3

        >>> lengthOfLongestSubstring("")
        0

        >>> lengthOfLongestSubstring(" ")
        1

        >>> lengthOfLongestSubstring(" b")
        2

        >>> lengthOfLongestSubstring(" b ")
        2

        >>> lengthOfLongestSubstring("ababab")
        2

        >>> lengthOfLongestSubstring("kpgvkcefkkrstuv")
        7

        >>> lengthOfLongestSubstring("abcdefghijklmaaabcdefghijklmnopqqqqqq")
        17

    """
    max_len, lower, upper = 0, 0, 0
    char_dict = {}

    for idx, char in enumerate(s):
        if char in char_dict:
            max_len = upper - lower if max_len < upper - lower else max_len

            # Get next char from it's previous occurance in string and reset lower bound.
            # Eg.  in "abba", since b is repeated, lower bound is s[2] --> 'ba' vs. 'bba'
            # whereas in "abaa", lower start bound is at s[1] --> 'ba'
            starting_idx = char_dict.get(char, "None")
            if char == s[starting_idx+1]:
                lower = idx
            elif lower <= starting_idx:
                # Eg. "uqinntq". During 5th iteration (2nd occurance of 'n')
                # lower = 4 and starting_idx = 1, we don't want to update the 'lower' value.
                lower = char_dict.get(s[starting_idx+1])

        char_dict[char] = idx
        upper += 1

    if max_len < upper - lower:
        max_len = upper - lower

    return max_len


if __name__ == "__main__":
    import doctest
    doctest.testmod()

# Pseudo Code:
# Need - a dictionary to store the unique chars, var for max length and an incrementing counter
# max = 0
# dict = {}
# counter = 0
# for char in string
#   if char not in dict,
#       add to dict
#       increment counter
#   else
#       if counter > max
#           max = counter
#
#       reset counter &
#       reset dict & add the char
# return max
