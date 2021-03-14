class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        freq = Counter(nums)
        candidates = set(nums)        
        
        result = sorted(candidates, key=lambda x: (-freq[x], x))
        
        return result[:k]