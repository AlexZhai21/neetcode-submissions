# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other_node):
        return self.val < other_node.val

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        ans = ListNode() #sneitnal node
        curr = ans
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(minHeap, lists[i])
        while minHeap:
            top = heapq.heappop(minHeap)
            der_next = top.next
            curr.next = top
            curr = curr.next
            if der_next:
                heapq.heappush(minHeap, der_next)
        return ans.next

        