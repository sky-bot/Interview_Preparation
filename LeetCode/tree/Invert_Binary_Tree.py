class Solution:
    def invertTree(self, root: TreeNode):
        if not root:
            return 
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        if root.right or root.left:
            root.left, root.right = root.right, root.left
        return root