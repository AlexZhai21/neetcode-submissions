# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def maxTrack(self, root, max_val):
            if root is None:
                return
            if root.val >= max_val:
                self.ans += 1
            maxTrack(self, root.left, max(max_val, root.val))
            maxTrack(self, root.right, max(max_val, root.val))

        maxTrack(self, root, root.val)
        return self.ans

        