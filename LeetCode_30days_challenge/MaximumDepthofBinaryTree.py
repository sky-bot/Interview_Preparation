class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.get_height(root, 0)
    
    def get_height(self, root, height):
        if root:
            height = height + 1
        else:
            return height
        
        left = self.get_height(root.left, height)
        right = self.get_height(root.right, height)
        
        return max(left, right)
        
