def max_profit(length, profit, capacity):

    dp = [[0 for i in range(capacity+1)] for j in range(len(length))]

    for i in range(capacity+1):
        dp[0][i] = i

    for i in range(len(length)):
        dp[i][0] = 0
    progress(dp)
    pass

def progress(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print(end='\n')

length = [1, 2, 3, 4, 5]
profit = [ [2, 6, 7, 10, 13]]
capacity = 5
print(max_profit(length, profit, capacity))