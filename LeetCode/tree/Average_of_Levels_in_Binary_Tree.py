class Solution:
    def averageOfLevels(self, root: TreeNode):
        S = list()
        level = 1

        result = list()
        S.append(root)
        
        while(S):
            level = len(S)
            total, i = 0, 0
            while(i < level):
                temp = S.pop(0)
                total += temp.val
                if temp.right:
                    S.append(temp.right)
                if temp.left:
                    S.append(temp.left)
                i += 1
            result.append(total/level)
        
        return result
             
             