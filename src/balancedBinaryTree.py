# brute force 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, depth):
            if not root:
                return depth
            
            left = dfs(root.left, depth+1)
            right = dfs(root.right, depth+1)

            return max(left, right)
        return dfs(root, 0)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if abs(left - right) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)