# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true


# def canConstruct(ransomNote, magazine):
#     mag_dict = dict()
#     for ch in magazine:
#         if mag_dict.get(ch):
#             mag_dict[ch] = mag_dict.get(ch) + 1
#         else:
#             mag_dict[ch] = 1   
    
#     for ch in ransomNote:
#         if ch in mag_dict.keys():
#             mag_dict[ch] = mag_dict[ch] - 1
#             if  mag_dict[ch] < 0:
#                 return False
#         else:
#             return False
    
#     return True

def canConstruct(RansomNote, Magazine):
    for ch in RansomNote:
        if ch in Magazine:
            Magazine = Magazine.replace(ch, "", 1)
        else:
            return False

RansomNote = "aa"
magzine = "aab"
print(canConstruct(RansomNote, magzine))

