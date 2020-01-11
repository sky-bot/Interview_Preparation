def isPossible(arr):
    requiredSum = sum(arr)

    if requiredSum%2 == 1:
        return False
    
    requiredSum = int(requiredSum / 2)

    print(requiredSum)
    arr = sorted(arr)
    mat = [[False for i in range(requiredSum+1) ] for j in range(len(arr)+1)]

    for i in range(1, len(arr)+1):
        mat[i][0] = True
    
    for i in range(requiredSum + 1):
        mat[0][i] = i
    
    
    mat[1][arr[0]] = True

    progress(mat)

    for i in range(2, len(arr)+2):
        for j in range(1, requiredSum+1):
            temp = mat[0][j]
            
    return progress


def progress(mat):
    for i in mat:
        print(i, end='\n')

isPossible([1,2,3,4])

