# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        odm = ListNode(-1)
        edm = ListNode(-1)

        o, e = odm, edm
        while h:
            if h.val%2 == 1:
                o.next = h
                o = o.next
            else:
                e.next = h
                e = e.next
            h = h.next

        e.next = None
        o.next = edm.next
        return odm.next


# varaition 1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, h: Optional[ListNode]) -> Optional[ListNode]:
        odm = ListNode(-1)
        edm = ListNode(-1)

        o, e = odm, edm
        pos = 1
        while h:
            if pos%2 == 1:
                o.next = h
                o = o.next
            else:
                e.next = h
                e = e.next
            h = h.next
            pos+=1

        e.next = None
        o.next = edm.next
        return odm.next

