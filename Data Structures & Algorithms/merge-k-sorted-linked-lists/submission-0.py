import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_heap = []
        dummy = ListNode()

        curr = dummy 
        for thing in lists:
            p = thing
            while p:
                heapq.heappush(my_heap, p.val)
                p = p.next
        while my_heap:
            curr.next = ListNode(heapq.heappop(my_heap))
            curr = curr.next
        return dummy.next

        