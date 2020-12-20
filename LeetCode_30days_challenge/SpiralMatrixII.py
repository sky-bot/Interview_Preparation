class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        
        mat = [[0 for j in range(n)] for i in range(n)]
        
        row_min=0
        row_max=n
        col_min=0
        col_max=n
        
        num = 1
        while(num <= (n*n)):
            
            for i in range(col_min, col_max):
                mat[row_min][i] = num
                num += 1
            row_min +=1
            
            for i in range(row_min, row_max):
                mat[i][col_max-1] = num
                num += 1
            col_max -= 1
            
            for i in range(col_max-1, col_min-1, -1):
                mat[row_max-1][i] = num
                num += 1
            row_max -= 1    

            print("Row_max: {}, Row_Min:{}, Col_max:{}, Col_min:{}".format(row_max, row_min,col_max,col_min))
            
            for i in range(row_max-1, row_min-1, -1):
                mat[i][col_min] = num
                num+=1
            col_min+=1
        
        return mat
        
