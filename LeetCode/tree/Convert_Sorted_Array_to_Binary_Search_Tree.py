class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        
        return self.convert(nums, 0, len(nums)-1)
    
    def convert(self, nums, left, right):
        if left > right:
            return None
        
        midpoint = int(left + (right - left) / 2)
        node = TreeNode(nums[midpoint])
        
        node.left = self.convert(nums, left, midpoint-1)
        node.right = self.convert(nums, midpoint+1, right)
        
        return node