
class Solution {
    private int goodNodes = 0;
    public int helper(TreeNode root, int max) {
        if(root != null){
            if(root.val >= max){
                goodNodes++;
                max = root.val;
            }
            helper(root.left, max);
            helper(root.right, max);
        }
        return goodNodes;
    }
    public int goodNodes(TreeNode root) {
        int result = helper(root, root.val);
        return result;
    }
}
