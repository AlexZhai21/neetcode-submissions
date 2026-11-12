# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def merge(self, l1, l2):
            if not l2:
                return l1
            ans = ListNode() #sneitnal
            curr = ans
            p1 = l1
            p2 = l2
            while p1 and p2:
                if p1.val < p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next

            if not p1:
                curr.next = p2
            else:
                curr.next = p1 #merging leftovers if the lenghts are differnt
            return ans.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #merge sort wauy, merge pairs of lists
        if not lists:
            return None

        while len(lists) > 1:
            mergedLists = [] #stores the heads of each sorted list
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                if i + 1 < len(lists):
                    l2 = lists[i + 1]
                mergedLists.append(self.merge(l1, l2))
            lists = mergedLists
        return lists[0]
        



        
        
        