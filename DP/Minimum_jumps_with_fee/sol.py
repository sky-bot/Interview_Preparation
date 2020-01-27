# Problem Statement #
# Given a staircase with ‘n’ steps and an array of ‘n’ numbers representing the fee that you have to pay if you take the step. Implement a method to calculate the minimum fee required to reach the top of the staircase (beyond the top-most step). At every step, you have an option to take either 1 step, 2 steps, or 3 steps. You should assume that you are standing at the first step.

# Example 1:
# Number of stairs (n) : 6
# Fee: {1,2,5,2,1,2}
# Output: 3
# Explanation: Starting from index '0', we can reach the top through: 0->3->top
# The total fee we have to pay will be (1+2).

# Example 2:
# Number of stairs (n): 4
# Fee: {2,3,4,5}
# Output: 5
# Explanation: Starting from index '0', we can reach the top through: 0->1->top
# The total fee we have to pay will be (2+3).

def minimum_fees(arr):
    dp = [0 for i in range(len(arr))]
    

    dp[0] = 0
    dp[1] = arr[0]
    dp[2] = arr[0]

    for i in range(3, len(arr)):
        dp[i] = min(dp[i-3]+arr[i-3], dp[i-2]+arr[i-2], dp[i-1]+arr[i-1])

    progress(dp)
    return dp[-1]

def progress(dp):
    for i in range(len(dp)):
        print(dp[i], end='\t')


fees = [2,3,4,5,1]
print('\n'+str(minimum_fees(fees)))
