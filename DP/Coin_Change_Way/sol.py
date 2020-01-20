def coin_change_ways(coins, val):
    dp = [[0 for i in range(val+1)] for j in range(len(coins)+1)]
    

    for i in range(1, val+1):
        dp[0][i] = i
        dp[1][i] = 1 if i%coins[0]==0 else 0 
    
    for i in range(len(coins)+1):
        dp[i][0] = 1
    
    
    # for i in range()
    progress(dp)
    pass

def progress(dp):
    for i in dp:
        for j in i:
            print(j, end='\t')
        print(end='\n')

coins = [1,2,3]
val = 5
print(coin_change_ways(coins, val))
