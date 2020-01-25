def min_jumps(arr):
    dp = [0 for i in range(len(arr))]

    for i in range(0, len(dp)):
        index_pos = arr[i]
        jump_till = dp[i]
        for j in range(i, i+index_pos+1):
            if j < len(dp) and dp[j]==0:
                dp[j]  = jump_till + 1

    progress(dp)
    return dp[-1]

def progress(dp):
    for i in range(len(dp)):
        print(dp[i], end='\t')

arr = [1,2,5,2,1,2]
print('\n'+str(min_jumps(arr)))
