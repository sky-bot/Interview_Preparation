class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.countSteps(root)
        
        return self.ans
    
    def countSteps(self, root):
        
        if not root:
            return 0
        
        leftSteps = self.countSteps(root.left)
        rightSteps = self.countSteps(root.right)
        
        print("Root Val: {}  leftSteps: {}  rightSteps: {}".format(root.val, leftSteps, rightSteps))
        self.ans += abs(leftSteps) + abs(rightSteps)
        
        return root.val + leftSteps + rightSteps - 1