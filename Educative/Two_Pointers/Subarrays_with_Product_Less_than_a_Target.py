# Problem Statement #
# Given an array with positive numbers and a target number, find all of its contiguous subarrays whose product is less than the target number.

# Example 1:

# Input: [2, 5, 3, 10], target=30 
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.
# Example 2:

# Input: [8, 2, 6, 5], target=50 
# Output: [8], [2], [8, 2], [6], [2, 6], [5], [6, 5] 
# Explanation: There are seven contiguous subarrays whose product is less than the target.


def find_subarrays(arr, target):
    result = []
    size = 1

    while(size < len(arr)):
        for i in range(0, len(arr)-size+1):
            _mul = give_mul(arr, i, size)

            if _mul < target:
                result.append(arr[i:i+size])
        size += 1


    return result

def give_mul(arr, index, size):
    _mul = 1
    for i in range(index, index+size):
        _mul = _mul * arr[i]
    return _mul

arr = [2, 5, 3, 10]
target = 30
print(find_subarrays(arr, target))