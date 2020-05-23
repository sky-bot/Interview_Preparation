class Solution:
    def findTarget(self, root: TreeNode, k: int):
        S = list()
        self.get_all_elements(root, S)
        print(S)
        result = False
        i, j = 0, len(S)-1
        while(i<j):
            print(i, j)
            if S[i] + S[j] == k:
                return True
            elif S[i] + S[j] < k:
                i += 1
            else:
                j -= 1
        
        return result
    
    def get_all_elements(self, root, S):
        if not root:
            return
        
        self.get_all_elements(root.left, S)
        S.append(root.val)
        # print(root.val)
        self.get_all_elements(root.right, S)
        
        return
        