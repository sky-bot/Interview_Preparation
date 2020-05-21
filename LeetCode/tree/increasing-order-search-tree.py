class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        head = None
        S = list()
        S.append(root)
        current = None
        while(S):
            last_ele = S[-1]
            
            if last_ele.left:
                S.append(last_ele.left)
                last_ele.left = None
                continue
            
            if last_ele.right:
                S.pop()
                S.append(last_ele.right)
                last_ele.right = None
                S.append(last_ele)
                continue
            
            if not head:
                head = last_ele
                tail = last_ele
                S.pop()
            else:
                tail.right = last_ele
                S.pop()
                tail = last_ele
                
        return head  