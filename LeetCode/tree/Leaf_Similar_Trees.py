class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        S1 = list()
        S2 = list()
        self.leaf_sequence(root1, S1)
        self.leaf_sequence(root2, S2)
        
        return S1==S2
    
    def leaf_sequence(self, root, S):
        if not root:
            return
        
        self.leaf_sequence(root.left, S)
        self.leaf_sequence(root.right, S)
        
        if root.left is None and root.right is None:
            S.append(root.val)
        return
        