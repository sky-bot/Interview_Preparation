class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = list()
        N = len(graph) - 1
        Q = [[0]]
        
        while Q:
            temp = Q.pop(0)
            if temp[-1]==N:
                result.append(temp)
            else:
                for neigbor in  graph[temp[-1]]:
                    Q.append(temp + [neigbor])
                
        return result
            