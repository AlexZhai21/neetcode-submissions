"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tracker = {}
        curr = head
        dummy = Node(x = 0)
        poo = dummy
        track = 0
        while curr:
            next_poo = Node(x = curr.val)
            poo.next = next_poo
            tracker[curr] = next_poo #<
            poo = poo.next
            curr = curr.next
            track += 1
        #this can recreate the list of the .next reelationships very simply
        re_curr = head
        ans_curr = dummy.next
        while re_curr:
            if re_curr.random:
                actual_random = tracker[re_curr.random] 
            else:
                actual_random = None
            ans_curr.random = actual_random
            ans_curr = ans_curr.next
            re_curr = re_curr.next
        return dummy.next



        
