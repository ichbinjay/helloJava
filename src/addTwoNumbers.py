# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = ""
        while l1:
            s = str(l1.val) + s
            l1 = l1.next
        a = int(s)
        s = ""
        while l2:
            s = str(l2.val) + s
            l2 = l2.next
        b = int(s)

        
        s = str(a + b)
        head = ListNode()
        curr = head
        for i in range(len(s)-1,-1,-1):
            curr.val = int(s[i])
            if i != 0:
                curr.next = ListNode()
                curr = curr.next
        return head

