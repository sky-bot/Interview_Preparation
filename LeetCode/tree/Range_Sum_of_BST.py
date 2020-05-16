# 938. Range Sum of BST


# Share
# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.

 

# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23
 

# Note:

# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        result = self.cal_sum(root, L, R, 0)
        
        return result
        
    def cal_sum(self, root, L, R, result):
        
        if not root:
            return result
        
        left = self.cal_sum(root.left, L, R, result)
        right = self.cal_sum(root.right, L, R, result)
        
        if root.val < L or root.val > R:
            return left + right
        
        return left + right + root.val