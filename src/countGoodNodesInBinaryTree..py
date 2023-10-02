class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodesCount = 0

        def helper(root, prevVal):
            nonlocal goodNodesCount
            if root:
                if root.val >= prevVal:
                    goodNodesCount += 1

                helper(root.left, max(root.val, prevVal))
                helper(root.right, max(root.val, prevVal))

        helper(root, root.val)

        return goodNodesCount


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    sol = Solution()
    print(sol.goodNodes(root))
