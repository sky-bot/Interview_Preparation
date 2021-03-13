class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        maxHeap = []
        
        for i in stones:
            heapq.heappush(maxHeap, -i)
        
        while(len(maxHeap)>1):
            print(maxHeap)
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            
            x = x - y
            
            if x!=0:
                heapq.heappush(maxHeap, x)
        
        return -heapq.heappop(maxHeap) if maxHeap else 0