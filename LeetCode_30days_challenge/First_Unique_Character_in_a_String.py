def firstUniqChar(self, s: str) -> int:
    frq_dict = dict()
    for ch in s:
        if frq_dict.get(ch):
            frq_dict[ch] = frq_dict[ch] + 1
        else:
            frq_dict[ch] = 1
    
    for i in range(len(s)):
        if frq_dict.get(s[i]) == 1:
            return i
        
    return -1

