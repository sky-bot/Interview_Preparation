

def target_sum(arr, target):
    total_sum = sum(arr)
    
    req_sum = int((total_sum + target) / 2)
    print(total_sum, target, req_sum)

    mat = [[0 for i in range(req_sum+1)] for j in range(len(arr)+1)]

    for i in range(req_sum+1):
        mat[0][i] = i
    
    for i in range(len(arr)+1):
        mat[i][0] = 1
    
    mat[1][arr[0]] = 1

    for i in range(2, len(arr)+1):
        for j in range(req_sum+1):
            mat[i][j] = mat[i-1][j] + mat[i-1][j - arr[i-1]] if j - arr[i - 1] >=0 else mat[i-1][j]

    progress(mat)
    
    return mat[-1][-1]
    

def progress(table):
    for row in table:
        print(row, end='\n')
    

target = 9
arr = [1, 2, 7, 1]
print(target_sum(arr, target))