class Solution:
    def nthUglyNumber(self, n: int) -> int:
        import heapq
        heapMin = [1]
        ans = 1 
        seen = set()
        limit=0
        
        while limit<n:
            limit+=1
            min_ele = heapq.heappop(heapMin)
            ans = min_ele
            a, b, c = 2*min_ele, 3*min_ele, 5*min_ele
            
            if a not in seen:
                seen.add(a)
                heapq.heappush(heapMin, a)
            
            if b not in seen:
                seen.add(b)
                heapq.heappush(heapMin, b)
            
            if c not in seen:
                seen.add(c)
                heapq.heappush(heapMin, c)
            
        return ans