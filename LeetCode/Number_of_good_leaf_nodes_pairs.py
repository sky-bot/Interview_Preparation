class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.count = 0
        self.inorder(root, distance)
        
        return self.count
    
    def inorder(self, root, distance):
        
        if not root:
            return [] 
        
        left = self.inorder(root.left, distance)
        right = self.inorder(root.right, distance)
        
        if not root.left and not root.right:
            return [1]
        
        for i in left:
            for j in right:
                if i + j <= distance:
                    self.count+=1
        
        final = [i+1 for i in left + right if i != 0]  
        
        return final