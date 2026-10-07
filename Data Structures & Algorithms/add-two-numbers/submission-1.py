# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum1 = 0
        sum2 = 0
        p1 = l1
        p1_m = 1
        while p1:
            sum1 += p1.val * p1_m
            p1 = p1.next
            p1_m *= 10
        p2 = l2
        p2_m = 1
        while p2:
            sum2 += p2.val * p2_m
            p2 = p2.next
            p2_m *= 10
        total = sum1 + sum2
        dummy = ListNode()
        curr = dummy
        if total == 0:
            curr.next = ListNode(val = 0)
            return dummy.next
        while total > 0:
            curr.next = ListNode(val = total % 10)
            curr = curr.next
            total = total // 10
        return dummy.next

        