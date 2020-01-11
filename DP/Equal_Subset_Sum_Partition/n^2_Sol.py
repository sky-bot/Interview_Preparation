def isPossible(arr):
    requiredSum = sum(arr)

    if requiredSum%2 == 1:
        return False
    
    requiredSum = int(requiredSum / 2)

    # print(requiredSum)
    arr = sorted(arr)
    mat = [[False for i in range(requiredSum+1) ] for j in range(len(arr)+1)]

    for i in range(1, len(arr)+1):
        mat[i][0] = True
    
    for i in range(requiredSum + 1):
        mat[0][i] = i
    
    
    mat[1][arr[0]] = True

    

    for i in range(2, len(arr)+1):
        for j in range(1, requiredSum+1):
            _sum = mat[0][j]
            print (_sum)
            val = mat[i-1][j-i]
            up_val = mat[i-1][_sum]
            mat[i][j] = up_val or val

    
    progress(mat)

    return progress


def progress(mat):
    for i in mat:
        print(i, end='\n')

isPossible([1,2,3,4])

