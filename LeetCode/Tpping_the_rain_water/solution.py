

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