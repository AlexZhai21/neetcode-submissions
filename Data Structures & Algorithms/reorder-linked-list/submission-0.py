# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        empty_dq = deque()
        p1 = head
        while p1:
            empty_dq.append(p1)
            p1 = p1.next
        tracker = 0
        while len(empty_dq) > 1:
            if tracker % 2 == 0: #even
                empty_dq.popleft().next = empty_dq[-1]
            elif tracker % 2 != 0: #odd
                empty_dq.pop().next = empty_dq[0]
            tracker += 1
        empty_dq[0].next = None
    
    

        # def recur_t(self, sent, prev, next_thing):
        #     if prev == None:
        #         return sent.next
        #     prev.next = next_thing
        #     return recur_t(self, sent, next_thing, prev.next)
        # p1 = sent
        # while p1 and p1.next:
        #     p1 = p1.next
        # next_thing = p1
        # return recur_t(self, sent, head, next_thing)


        