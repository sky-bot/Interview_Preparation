# Problem Statement #
# Given a number array representing the wealth of ‘n’ houses, determine the maximum amount of money the thief can steal without alerting the security system.

# Example 1:

# Input: {2, 5, 1, 3, 6, 2, 4}
# Output: 15
# Explanation: The thief should steal from houses 5 + 6 + 4
# Example 2:

# Input: {2, 10, 14, 8, 1}
# Output: 18
# Explanation: The thief should steal from houses 10 + 8
# solution
#==============

def max_profit(arr):
    dp = [0 for i in arr]

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        dp[i] = max(dp[i-1], dp[i-2]+arr[i])

    progress(dp)
    return dp[-1]

def progress(arr):
    for i in arr:
        print(i, end='\t')

arr = [2, 5, 1, 3, 6, 2, 4]
print('\n'+str(max_profit(arr)))
