# Comparing Strings containing Backspaces (medium) #
# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:

# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:

# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.

# Sol


def backspace_compare(str1, str2):
    a = remove_backspace(str1)
    b = remove_backspace(str2)

    return False if a != b else True

def remove_backspace(spaced):
    spaced = list(spaced)
    backspace = 0

    for i in range(len(spaced)-1, -1, -1):
        if spaced[i] == '#':
            backspace += 1
            spaced[i] = '_'
            continue
        
        if backspace > 0:
            spaced[i] = '_'
            backspace -= 1
        
    result = "".join(spaced).replace("_", "")
    return result
    

str1="xywrrmp"
str2="xywrrmu#p"
print(backspace_compare(str1, str2))