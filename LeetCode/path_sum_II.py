class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        all_paths = list()
        self.inorder(root, [], 0, all_paths, targetSum)
        
        return all_paths
        
        
    
    def inorder(self, root, list_till_now, sum_till_now ,all_paths, target):
        if not root:
            return
        else:
            if sum_till_now + root.val == target and root.left is None and root.right is None:
                list_till_now.append(root.val)
                all_paths.append(list_till_now)
            
            self.inorder(root.left, list_till_now + [root.val], sum_till_now + root.val ,all_paths, target)
            print(root.val)
            self.inorder(root.right, list_till_now + [root.val], sum_till_now + root.val ,all_paths, target)
            
            return