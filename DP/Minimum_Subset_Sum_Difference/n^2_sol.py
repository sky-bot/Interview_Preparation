from math import ceil
def min_diff(arr):
    req_sum = ceil(sum(arr)/2)-1
    print(req_sum)
    mat = [[False for i in range(req_sum+1)] for i in range(len(arr)+1)]
   
    
    for i in range(req_sum+1):
        mat[0][i] = i
    for i in range(1, len(arr)+1):
        mat[i][0] = True

    mat[1][arr[0]] = True

    for i in range(2, len(arr)+1):
        for j in range(1, req_sum+1):
            _sum = arr[i-1]
  
            mat[i][j] = mat[i-1][j] or mat[i-1][j-_sum] if j-_sum >= 0 else mat[i-1][j]
            

    print(mat[-1])
    pass






def progress(mat):
    for i in mat:
        print(i, end='\n')

arr = [1, 2, 3, 9]
print(min_diff(arr))