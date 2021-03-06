def SubsetCount(arr, target):
    table = [[0 for i in range(target +1)] for j in range(len(arr)+1)]
    table[0] = [i for i in range(target+1)]
    for i in range(1, len(arr)+1):
        table[i][0] = 1
    
    table[1][arr[0]] = 1

    for i in range(2, len(arr)+1):
        for j in range(1, target+1):
            exclude = table[i-1][j]
            include = table[i-1][j-arr[i-1]] + exclude if j-arr[i-1] >=0 else exclude
            table[i][j] = include
            


    progress(table)
    return table[-1][-1]

def progress(table):
    for row in table:
        print(row, end='\n')

arr = [1,1,2,3]
target = 4
print(SubsetCount(arr, target))
