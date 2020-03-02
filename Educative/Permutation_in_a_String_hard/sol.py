# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n!n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.

# Sol
def find_permutation(str, pattern):
    print("str => {}  pattern => {}".format(str, pattern))
    pat_dict = dict()

    for i in pattern:
        if i in pat_dict.keys():
            pat_dict[i] = pat_dict[i] + 1
        else:
            pat_dict[i] = 1

    for i in range(len(str)):
        if str[i] in pat_dict.keys():
            pat_dict[str[i]] = pat_dict[str[i]]-1
        else:
            return False
    
    for i in pat_dict.values():
        if i != 0:
            return False

    return True



def main():
    str = "bcdxabcdy"
    pattern = "bcdyabcdx"
    for i in range(len(str)):
        if i+len(pattern)<=len(str):
            temp_val = find_permutation(str[i:i+len(pattern)], pattern)
            # print(temp_val)
        if temp_val:
            return True
    return False

print(main())