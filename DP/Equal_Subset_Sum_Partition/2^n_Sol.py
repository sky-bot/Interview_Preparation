def canPartition(arr):
    total_sum = sum(arr)
    if total_sum%2==0:
        return recur(total_sum/2, arr, 0, 0)
    else:
        return False

def recur(requirdSum, arr, index, sum):
    if index >= len(arr):
        return False

    if requirdSum == sum:
        return True

    inclu = recur(requirdSum, arr, index+1, sum+arr[index])
    exclu = recur(requirdSum, arr, index+1, sum)

    return inclu or exclu


print (canPartition([1,2,3,4,1,1])) 