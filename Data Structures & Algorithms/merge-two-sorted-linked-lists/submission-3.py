# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        head = ListNode()
        
        prev = head #the newest addition to the sorted list
        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next
            if p1.val <= p2.val:
                prev.next = p1
                prev = p1
                p1 = p1_next
            else: #p1.val > p2.val
                prev.next = p2
                prev = p2
                p2 = p2_next
        #after this loop ends, either p1 or p2 has been gone.
        if p1: #if p1 is still here
            prev.next = p1
        else:
            prev.next = p2
        return head.next
        

        



        