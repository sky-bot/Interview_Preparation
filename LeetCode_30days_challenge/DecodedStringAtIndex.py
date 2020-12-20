class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        length = 0
        for i in range(len(S)):
            if S[i].isalpha():
                length += 1
            else:
                length *= int(S[i])
            
        for i in range(len(S)-1, -1, -1):
            K = K%length
            
            if K == 0 and S[i].isalpha():
                return S[i]
            
            if S[i].isalpha():
                length -= 1
            else:
                length /= int(S[i])
        
        return -1
