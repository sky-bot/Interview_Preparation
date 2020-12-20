class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod = [0] * 60
        count = 0
        
        for i in time:
            count = count + mod[-i%60]
            mod[i%60]+=1          
            
        return count
