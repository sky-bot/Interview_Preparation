class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> s = new Stack<>();
        if(root == null) return res;
        s.push(root);
        TreeNode curr = root.left;
        while(!s.isEmpty()){
            if(curr != null){
                s.push(curr);
                curr = curr.left;
            } else {
                TreeNode n = s.pop();
                res.add(n.val);
                if(n.right != null){
                    s.push(n.right);
                    curr = n.right.left;
                }
            }    
            // System.out.print("t : " + s.peek().val);
        }
        return res;
    }
}