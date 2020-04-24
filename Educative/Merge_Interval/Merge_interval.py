# Problem Statement #
# Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

# Example 1:

# Intervals: [[1,4], [2,5], [7,9]]
# Output: [[1,5], [7,9]]
# Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into 
# one [1,5].

# Example 2:

# Intervals: [[6,7], [2,4], [5,9]]
# Output: [[2,4], [5,9]]
# Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].
 
# Example 3:

# Intervals: [[1,4], [2,6], [3,5]]
# Output: [[1,6]]
# Explanation: Since all the given intervals overlap, we merged them into one.

from operator import itemgetter 


def merge_interval(arr):
    arr = sorted(arr, key=itemgetter(0))
    i = 0 
    while i < len(arr)-1:
        temp = merge(arr.pop(i), arr.pop(i))
        if len(temp) > 1:
            arr.insert(i, temp[0])
            arr.insert(i+1, temp[1])
            i += 1
        else:
            arr.insert(i, temp[0])
    
    return arr

def merge(a, b):
    if a[1] < b[0]:
        return [a, b]
    
    if a[1] <= b[1]:
        return [[a[0], b[1]]]
    else:
        return [a]


# arr = [[1,4], [2,5], [7,9]]
arr = [[1,4], [2,6], [3,5]]
print(merge_interval(arr))

