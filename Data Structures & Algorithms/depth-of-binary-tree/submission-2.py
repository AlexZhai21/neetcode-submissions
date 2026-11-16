# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #bfs
        q = deque([])

        if root:
            q.append([root, 1])
        else:
            return 0
        level = 0
        while q:
            node, lev = q.popleft() #the node
            level = max(level, lev)
            if node.left:
                q.append([node.left, lev + 1])
            if node.right:
                q.append([node.right, lev + 1])
        return level

