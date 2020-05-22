class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        S = list()
        st = ""
        self.convert(root, st, S)
        _sum = 0
        for ele in S:
            _sum += int(ele, 2)
        return _sum
    
    def convert(self, root, st, S):
        if not root:
            return
        st = "{}{}".format(st, root.val)
        self.convert(root.left, st, S)
        self.convert(root.right, st, S)
        
        if root.left is None and root.right is None:
            S.append(st)
        return 
