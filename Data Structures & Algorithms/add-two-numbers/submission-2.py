# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        p1 = l1
        p2 = l2
        while p1 or p2 or carry > 0:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            curr_val = p1_val + p2_val + carry
            carry = curr_val // 10
            if curr_val >= 10:
                curr_val = curr_val % 10
            curr.next = ListNode(val = curr_val)
            curr = curr.next
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
        return dummy.next


            
            
        