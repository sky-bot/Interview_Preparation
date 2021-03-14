class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import Counter
        import heapq
        
        freq = Counter(words)
        
        result = []
        
        for key, val in freq.items():
            heapq.heappush(result, [-val, key])
        
        final_result = list()
        for i in range(k):
            _, key = heapq.heappop(result)
            final_result.append(key)
        
        return final_result
        