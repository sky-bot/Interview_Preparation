def SubsetCount(arr, target):
    table = [[0 for i in range(target +1)] for j in range(len(arr)+1)]
    table[0] = [i for i in range(target+1)]
    for i in range(1, len(arr)+1):
        table[i][0] = 1
    
    table[1][arr[0]] = 1

    for i in range(2, len(arr)+1):
        for j in range(1, target+1):
            # exclu = table[i -1][j]
            table[i][j] = table[i-1][j - arr[i-1]] + table[i -1][j]
            # table[i][j] = max(exclu, include)
            


    progress(table)
    return table[-1][-1]

def progress(table):
    for row in table:
        print(row, end='\n')





arr = [1, 2, 7, 1, 5]
target = 9
print(SubsetCount(arr, target))