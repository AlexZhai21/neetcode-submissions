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
        new_head = None
        n_curr = curr
        ks_done = 0
        s_start = start
        while end:
            for i in range(k):
                if end:
                    end = end.next
                else:
                    return new_head
            ks_done += 1
            while n_curr != end: #linked list reversal
                n_curr = curr.next
                curr.next = prev
                prev = curr
                curr = n_curr
            if not new_head: #setting the new head (first time only)
                new_head = prev
            
            start.next = end
            
            if s_start != start:
                s_start.next = prev #s_start is the initial start
                s_start = start
            start = end
        return new_head



            
            

        