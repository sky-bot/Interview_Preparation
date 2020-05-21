class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        S = list()
        S.append(root)
        target = root.val
        result = True
        while(S):
            last_ele = S.pop()
            if last_ele.val != target:
                return False
            
            if last_ele.left:
                S.append(last_ele.left)

            if last_ele.right:
                S.append(last_ele.right)
            
        return result