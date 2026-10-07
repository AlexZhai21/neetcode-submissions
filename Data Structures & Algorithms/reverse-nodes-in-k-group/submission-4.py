# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sent = ListNode(next = head)
        p1 = sent
        p2 = sent.next
        new_end = p1
        while True:
            temp = new_end
            for i in range(k):
                if temp and temp.next:
                    temp = temp.next
                else:
                    return sent.next
            #after this, temp will be poinintg at the last node in the k group
            
            while p1 != temp:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
                #after this, p1 is the last item in your k group and p2 is the first element in the next group
            new_end_n = new_end.next
            new_end.next = p1
            new_end = new_end_n
            new_end.next = p2
            print(p1.val)
        return sent.next

        #s -> 1 -> 2 -> 3 ->4 -> 5 -> 6

        
        