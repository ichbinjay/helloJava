class Solution {
    public TreeNode helper(TreeNode root) {
        if (root != null) {
            TreeNode temp = root.left;
            root.left = helper(root.right);
            root.right = helper(temp);
            return root;
        } else {
            return null;
        }
    }

    public TreeNode invertTree(TreeNode root) {
        return helper(root);
    }
}
