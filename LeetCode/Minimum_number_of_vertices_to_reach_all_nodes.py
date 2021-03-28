class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        reach = set()
        for i in edges:
            reach.add(i[1])
        
        ans = set()
        for i in range(n):
            if not i in reach:
                ans.add(i)
        
        return ans
                