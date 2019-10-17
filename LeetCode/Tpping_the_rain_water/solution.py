# Question:- Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which 
# together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# Solution:-> O(n)

def maxArea(height):
    maxarea = 0
    left = 0
    right = len(height)-1
    disApart = right - left
    
    while(left<right):
        maxhigh = max(height[left], height[right])
        minHeight = min(height[left], height[right])
        
        tempArea = disApart * minHeight
        
        maxarea = tempArea if tempArea > maxarea else maxarea
        
        if maxhigh == height[left]:
            right = right - 1
        else:
            left = left + 1
        disApart = disApart - 1 
    return maxarea