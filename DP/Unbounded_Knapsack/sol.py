def Unbounded_Knapsack(weight, profit, capacity):

    dp = [[0 for i in range(capacity+1)] for j in range(len(profit)+1)]

    for i in range(capacity+1):
        dp[0][i] = i
    
    

    for i in range(capacity+1):
        dp[1][i] = i*profit[0] 

    for i in range(2, len(profit)+1):

        temp_step = 0
        for j in range(1, capacity+1):
            if j%weight[i-1]==0:
                dp[i][j] = max(dp[i][j -  weight[i-1]]+ profit[i-1], dp[i-1][j])
                temp_step = dp[i][j]
            else:
                dp[i][j] = temp_step + dp[i-1][j%weight[i-1]] 
                print(i,j)
        

    progress(dp)
    return dp[-1][-1]




def progress(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print(end='\n')















weight = [1,3,4,5]
profit = [15,50,60,90]
capacity = 8
print(Unbounded_Knapsack(weight, profit, capacity))