# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def preorder(root, maxE):
            if root:
                nonlocal count
                if root.val >= maxE:
                    maxE = root.val
                    count += 1

                preorder(root.left, maxE)
                preorder(root.right, maxE)
        
        preorder(root, root.val)
        return count


            
        

            
