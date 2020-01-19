def Unbounded_Knapsack(weight, profit, capacity):

    dp = [[0 for i in range(capacity+1)] for j in range(len(profit)+1)]

    for i in range(capacity+1):
        dp[0][i] = i



    progress(dp)
    pass




def progress(dp):
    for i in dp:
        print(i, end='\n')















weight = [1,3,4,5]
profit = [15,50,60,90]
capacity = 8
print(Unbounded_Knapsack(weight, profit, capacity))