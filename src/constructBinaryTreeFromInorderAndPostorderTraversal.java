class Solution {
    private int inPos;
    
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        inPos = inorder.length - 1;
        return buildTreeHelper(inorder, postorder, 0, inorder.length - 1);
    }
    
    private TreeNode buildTreeHelper(int[] inorder, int[] postorder, int inStart, int inEnd) {
        if (inStart > inEnd) {
            return null;
        }
        
        TreeNode root = new TreeNode(postorder[inPos--]);
        int rootIdx = findIndex(inorder, root.val, inStart, inEnd);
        root.right = buildTreeHelper(inorder, postorder, rootIdx + 1, inEnd);
        root.left = buildTreeHelper(inorder, postorder, inStart, rootIdx - 1);
        return root;
    }
    
    private int findIndex(int[] inorder, int val, int start, int end) {
        for (int i = start; i <= end; i++) {
            if (inorder[i] == val) {
                return i;
            }
        }
        return -1;
    }
}