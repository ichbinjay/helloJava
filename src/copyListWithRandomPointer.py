"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(-1)
        cur = dummy
        nodeMap = {}
        while head:
            if head not in nodeMap:
                nodeMap[head] = Node(head.val)
            cur.next = nodeMap[head]
            if head.random:
                if head.random not in nodeMap:
                    nodeMap[head.random] = Node(head.random.val)
                cur.next.random = nodeMap[head.random]
            head = head.next
            cur = cur.next
        return dummy.next