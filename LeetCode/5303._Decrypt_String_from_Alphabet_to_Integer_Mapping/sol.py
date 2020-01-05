# 5303. Decrypt String from Alphabet to Integer Mapping

# Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

# Characters ('a' to 'i') are represented by ('1' to '9') respectively.
# Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
# Return the string formed after mapping.

# It's guaranteed that a unique mapping will always exist.

 

# Example 1:

# Input: s = "10#11#12"
# Output: "jkab"
# Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
# Example 2:

# Input: s = "1326#"
# Output: "acz"
# Example 3:

# Input: s = "25#"
# Output: "y"
# Example 4:

# Input: s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
# Output: "abcdefghijklmnopqrstuvwxyz"

# Solution:
class Solution:
    def freqAlphabets(self, s: str) -> str:
        code = dict()
        init = 96
        for i in range(1, 10):
            code[str(i)] = chr(init+i)
    
        for i in range(10, 27):
            code[str(i)+'#'] = chr(init + i)
        slen = len(s)
        result = ""
        i = 0
        while(i < slen):
            upper = i+3
            if upper <=slen and s[i:upper] in code.keys():
                result = result + code[s[i:upper]]
                i = i + 3
            else:
                result = result + code[s[i]]
                i = i + 1
            
        return result