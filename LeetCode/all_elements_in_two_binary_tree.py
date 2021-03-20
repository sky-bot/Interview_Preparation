class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        result = []
        self.inorder(root1, result)
        self.inorder(root2, result)
        
        return sorted(result)
    
    def inorder(self, root, result): 
        if not root:
            return
        
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
        
        return