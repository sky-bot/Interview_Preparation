# Problem Statement #
# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:

# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:

# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.
#Sol

def triplet_sum_close_to_target(arr, target_sum):
    first=0
    diff = 10000000
    arr.sort()
    result = 0
    while (first <= len(arr)-2):
        second = first + 1
        third = len(arr)-1
        
        while(second<third):
            temp = [arr[first], arr[second], arr[third]]
            _sum = arr[first] + arr[second] + arr[third]
            temp_diff = target_sum - _sum if target_sum - _sum > 0 else -1*(target_sum - _sum)
            if diff > temp_diff:
                result = _sum
                diff = temp_diff
                second = second +1
            else: 
                third = third - 1
            
        first = first + 1
    return result


arr = [1, 0, 1, 1]
target = 100
print(triplet_sum_close_to_target(arr, target))