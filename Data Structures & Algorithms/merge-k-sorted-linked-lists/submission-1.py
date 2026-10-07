import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        min_heap = []
        for thing in lists:
            if thing:
                heapq.heappush(min_heap, NodeWrapper(thing))
        while min_heap:
            curr.next = heapq.heappop(min_heap).node
            curr = curr.next
            if curr.next:
                heapq.heappush(min_heap, NodeWrapper(curr.next))
        return dummy.next
            


        
        
        