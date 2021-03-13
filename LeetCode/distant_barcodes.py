class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        import heapq
        
        freq_count = Counter(barcodes)

        maxHeap = list()
        
        for char, freq in freq_count.items():
            heapq.heappush(maxHeap, [-freq, char])
        
        result = list()
        pre_char = None
        pre_freq = 0
        
        while(maxHeap):
            
            freq, char = heapq.heappop(maxHeap)
            
            if pre_char and -pre_freq > 0:
                heapq.heappush(maxHeap, [pre_freq, pre_char])
            
            result.append(char)
            pre_char = char
            pre_freq = freq + 1
        
        return result