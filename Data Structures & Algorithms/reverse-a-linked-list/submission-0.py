# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sent = ListNode(next = head)
        p1 = head
        if p1:
            p2 = head.next 
        while p1 and p2:
            
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        if head:
            head.next = None
        return p1


        