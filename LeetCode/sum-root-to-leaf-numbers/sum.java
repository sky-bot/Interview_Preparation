/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public int sumNumbers(TreeNode root) {
    
    int sum = 0;
    sum = rec(root, sum);
        
    return sum;
        
    }
    
    public int rec(TreeNode root, int sum)
    {
        if(root==null)return 0;
        sum = root.val + sum;
        int left =rec(root.left, sum*10);
        int right = rec(root.right, sum*10);
        
        return (sum > left+right ? sum: left+right);
    }
}