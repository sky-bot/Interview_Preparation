

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

    progress(mat)
    

    
    pass
    

def progress(table):
    for row in table:
        print(row, end='\n')
    

















target = 1
arr = [1, 1, 2, 3]
target_sum(arr, target)