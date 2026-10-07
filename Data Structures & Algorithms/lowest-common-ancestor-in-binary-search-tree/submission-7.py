# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tracker = {}
        bfs = deque()
        bfs.append(root)
        tracker[root] = [root]
        while bfs:
            to_remove = bfs.popleft()
            if p.val < to_remove.val or q.val < to_remove.val:
                if to_remove.left:
                    bfs.append(to_remove.left)
        
                    tracker[to_remove.left] = tracker[to_remove] + [to_remove.left]
            if p.val > to_remove.val or q.val > to_remove.val:
                if to_remove.right:
                    bfs.append(to_remove.right)
                    tracker[to_remove.right] = tracker[to_remove] + [to_remove.right]
            if p in tracker and q in tracker:
                break
        p_thing = tracker[p]
        q_thing = tracker[q]
        similar = [i for i in p_thing if i in q_thing]
        return similar[-1]


        