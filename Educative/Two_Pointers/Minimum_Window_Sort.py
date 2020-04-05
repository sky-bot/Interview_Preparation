# Minimum Window Sort (medium) #
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example 1:

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
# Example 3:

# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted
# Example 4:

# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.
# Sol

def shortest_window_sort(arr):
    temp_min_index = 0 
    temp_max_Index = 0

    for i in range(0, len(arr)-1):
        if arr[i] > arr[i+1]:
            temp_min_index = i
            break

    for i in range(len(arr)-1, 0, -1):
        if arr[i] < arr[i-1]:
            temp_max_Index = i
            break
    result = check_out_bounds(temp_min_index, temp_max_Index, arr) 

    return result

def check_out_bounds(min_index, max_index, arr):
    sub_array = arr[min_index:max_index+1]
    min_in_sub = min(sub_array)
    max_in_sub = max(sub_array)
    actual_min_index = min_index
    actual_max_index = max_index
    for i in range(min_index-1, -1, -1):
        if arr[i] > min_in_sub:
            actual_min_index = i
    
    for i in range(max_index+1, len(arr)):
        if arr[i] < max_in_sub:
            actual_max_index = i

    return 0 if (actual_min_index==0 and actual_max_index==0) else len(arr[actual_min_index:actual_max_index+1])

arr = [3, 2, 1]
print(shortest_window_sort(arr))