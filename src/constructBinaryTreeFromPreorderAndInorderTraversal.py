class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional


class Solution:
    pos = 0

    def buildTree(self, po: List[int], io: List[int]) -> Optional[TreeNode]:
        if not io:
            return None

        ind = 0
        target = po[self.pos]
        for i in range(len(io)):
            if target == io[i]:
                ind = i
                self.pos += 1
                break
        root = TreeNode(io[ind])
        root.left = self.buildTree(po, io[:ind])
        root.right = self.buildTree(po, io[ind + 1:])

        return root


s = Solution()
s.buildTree([3,9,20,15,7],[9,3,15,20,7])
