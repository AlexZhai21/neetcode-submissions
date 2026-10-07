# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev = None
        start = head
        curr = start
        end = head
        n_curr = curr
        dummy = ListNode(next = head)
        s_start = dummy
        while end:
            for i in range(k):
                if end:
                    end = end.next
                else:
                    return dummy.next
            while n_curr != end: #linked list reversal
                n_curr = curr.next
                curr.next = prev
                prev = curr
                curr = n_curr
            s_start.next = prev
            s_start = start
            start.next = end
            start = end
            
        return dummy.next
        
        



            
            

        