# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sent = ListNode(next = head)
        fast = sent
        slow = sent
        while fast and fast.next:
            fast= fast.next.next
            slow = slow.next
            if fast and fast == slow:
                return True
        return False

        