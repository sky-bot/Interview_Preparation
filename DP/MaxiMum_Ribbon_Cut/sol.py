def max_ribbon(ribbon, val):
    dp = [[0 for i in range(val+1)] for j in range(len(ribbon)+1)]

    for i in range(val+1):
        dp[0][i] = i
        dp[1][i] =  int(i/ribbon[0]) if i%ribbon[0]==0 else 0

    for i in range(2, len(ribbon)+1):
        for j in range(1, val+1):
            dp[i][j] = max(dp[i-1][j], dp[i][j-ribbon[i-1]]+1) if j-ribbon[i-1] >=0 else dp[i-1][j]

    progress(dp)
    pass

def progress(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print(end='\n')



ribbon = [3,5,7]
val = 13
print(max_ribbon(ribbon, val))
