# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(self, curr, p, q):
            if p.val > curr.val and q.val > curr.val:#both p and q are both in the right subtree
                return dfs(self, curr.right, p, q)
            elif p.val < curr.val and q.val < curr.val:
                return dfs(self, curr.left, p, q)
            else:
                return curr
        return dfs(self, root, p,q)