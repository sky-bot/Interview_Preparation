class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        result = self.find(root, p, q)
        return result
        
    def find(self, root, p, q):
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)
        
        if not left and not right:
            return None
        if left and right:
            return root
        
        return left or right
        