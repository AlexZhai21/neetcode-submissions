# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #afterwards, slow will be in the middle of the list.
        rev = slow
        n_rev = rev.next
        rev.next = None
        while rev and n_rev:
            actual_n_rev = n_rev.next
            n_rev.next = rev
            rev = n_rev
            n_rev = actual_n_rev
        #after this, the second half should be reversed
        #rev = tail
        def recur_t(self, prev, next_thing):
            a_next_thing = prev.next
            prev.next = next_thing
            if next_thing == None:
                return
            return recur_t(self, next_thing, a_next_thing)
        return recur_t(self, head, rev)

        
        

        


       
    
    


        

        