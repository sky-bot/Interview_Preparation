class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        rec(root, res);
        return res;
    }
    
    public void rec(TreeNode root, List<Integer> res){
        if(root == null) return;        
        rec(root.left, res);
        res.add(root.val);
        rec(root.right, res);
        return;
    }
}