class Solution:
    def reorganizeString(self, S: str) -> str:
        import heapq
        from collections import Counter
        
        frequencies = Counter(S)
        maxHeap = list()
        
        for key, count in frequencies.items():
            heapq.heappush(maxHeap, [-count, key])
        
        previous_char = None
        previous_freq = 0
        result=[]
        
        while(maxHeap):
            
            freq, char = heapq.heappop(maxHeap)
            
            if previous_char and -previous_freq > 0:
                heapq.heappush(maxHeap, [previous_freq, previous_char])
            
            result.append(char)
            previous_char = char
            previous_freq = freq + 1
            
        return "".join(result) if len(result) == len(S) else ""