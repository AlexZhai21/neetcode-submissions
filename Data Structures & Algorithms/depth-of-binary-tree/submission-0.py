# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def recurDepth(self, ans, root):
            if root is None:
                return ans
            return max(recurDepth(self, ans + 1, root.left), recurDepth(self, ans + 1, root.right))
        
        return recurDepth(self, 0, root)
        