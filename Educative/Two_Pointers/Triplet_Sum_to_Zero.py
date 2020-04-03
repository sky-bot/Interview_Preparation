# Problem Statement #
# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.
#Sol

def search_triplets(arr):
    arr.sort()
    triplets = []
    result = []
    first = 0

    while(first!=len(arr)-2):
        sec = first+1
        thi = len(arr)-1

        while(sec<thi):
            _sum = arr[first]+arr[sec]+arr[thi]
            if _sum == 0:
                if triplets:
                    if triplets[-1]!=[arr[first], arr[sec], arr[thi]]:
                        triplets.append([arr[first], arr[sec], arr[thi]])                    
                else:
                    triplets.append([arr[first], arr[sec], arr[thi]])
            
            if _sum > 0:
                thi = thi - 1
            else:
                sec = sec + 1
        first = first + 1
                
    return triplets

arr = [-3, 0, 1, 2, -1, 1, -2]
print(search_triplets(arr))
