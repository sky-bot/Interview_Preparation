from collections import deque
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        up = 0
        down = len(isWater) -1
        left = 0
        right = len(isWater[0])-1
        Q = deque()
        
        for i in range(len(isWater)):
            for j in range(len(isWater[i])):
                if isWater[i][j]==1:
                    isWater[i][j] = 0 
                    Q.append((i, j))
                else:
                    isWater[i][j] = -1
        
        while Q:
            row, col = Q.popleft()
            val = isWater[row][col]
            
            temp = [-1, 0, 1, 0, -1]
            
            for i in range(4):

                if (row+temp[i]>=0 and row+temp[i]<=down
                    and col+temp[i+1]>=0 and col+temp[i+1]<=right):
                    
                    if isWater[row+temp[i]][col+temp[i+1]]==-1:
                        isWater[row+temp[i]][col+temp[i+1]] = val + 1
                        Q.append((row+temp[i], col+temp[i+1]))
        
        return isWater