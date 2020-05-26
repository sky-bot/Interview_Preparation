class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count = 0
        self.cal(root, sum, 0)
        return int((self.count+1)/2)
    
    def cal(self, root, sum, till):
        if not root:
            return
        
        cur_till = till + root.val
        print(root.val, till)
        if cur_till == sum:
            print(root.val)
            self.count += 1
        elif cur_till > sum:
            self.cal(root.left, sum, 0)
            self.cal(root.right, sum, 0)
        elif cur_till < sum:
            # print(till, sum)
            self.cal(root.left, sum, root.val)
            self.cal(root.right, sum, root.val)
            self.cal(root.left, sum, cur_till)
            self.cal(root.right, sum, cur_till)
        
            
        return