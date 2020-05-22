class Solution:
    def maxDepth(self, root: TreeNode):
        result = self.calculate(root, 0)
        return result
    
    def calculate(self, root, height):
        if not root:
            return height
        height += 1
        
        return max(self.calculate(root.left, height), self.calculate(root.right, height))