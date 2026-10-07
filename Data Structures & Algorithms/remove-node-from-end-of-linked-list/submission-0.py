# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sent = ListNode(next = head)
        extra_slow = sent
        fast, slow = head, head
        for i in range(n):
            fast = fast.next
        #after this, fast is now n steps ahead of slow
        while fast:
            fast = fast.next
            slow = slow.next
            extra_slow = extra_slow.next
        #after this, slow is now at the nth node from the end of the list
        extra_slow.next = slow.next
        return sent.next

        