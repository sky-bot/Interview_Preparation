class Solution:
    found = False
    our_root = None
    dummy = TreeNode(0)
    head = dummy.right
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.inorder(root)
        return self.our_root
    
    def inorder(self, root):
        if root is None:
            return
        
        self.inorder(root.left)
        
        if not self.found:
            self.our_root = root
            self.found = True
        
        root.left = None
        self.dummy.right = root
        self.dummy = root
        self.inorder(root.right)
        
        return
