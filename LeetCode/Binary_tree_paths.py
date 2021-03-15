class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        all_paths = list()
        
        if root.left is None and root.right is None:
            return [str(root.val)]
        
        
        self.inorder(root.left, str(root.val), all_paths)
        self.inorder(root.right, str(root.val), all_paths)
        
        return all_paths
    
    def inorder(self, root, current_path, all_paths):
        if not root:
            return 

        if root.left is None and root.right is None:
            all_paths.append(current_path+"->"+str(root.val))
            return
        else:
            self.inorder(root.left, current_path+"->"+str(root.val), all_paths)
            print(root.val)
            self.inorder(root.right, current_path+"->"+str(root.val), all_paths)
            return