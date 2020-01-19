def max_profit(length, profit, capacity):

    dp = [[0 for i in range(capacity+1)] for j in range(len(length)+1)]
    # print(profit[0], profit)
    for i in range(capacity+1):
        dp[0][i] = i
        dp[1][i] = i*profit[0]
        # print(profit[0])

    for i in range(len(length)):
        dp[i][0] = 0
    # print(capacity)
    for i in range(2, len(profit)+1):
        temp_step = 0
        
        for j in range(1, capacity+1):
            if j%length[i-1]==0:
                
                dp[i][j] = max(dp[i-1][j], dp[i][j-length[i-1]]+profit[i-1])
                temp_step = dp[i][j]
            else:
                dp[i][j] = max(temp_step + dp[i-1][j%length[i-1]], dp[i-1][j])  
    
    progress(dp)
    return dp[-1][-1]

def progress(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print(end='\n')

length = [1, 2, 3, 4, 5]
profit = [2, 6, 7, 10, 13]
capacity = 5
print(max_profit(length, profit, capacity))