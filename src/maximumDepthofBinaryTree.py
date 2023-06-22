class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            left_depth = dfs(root.left, depth + 1)
            right_depth = dfs(root.right, depth + 1)
            return max(left_depth, right_depth)
        return dfs(root, 0)