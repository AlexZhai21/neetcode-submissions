# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        tracker = {}
        #choices: dp(leftchild) + dp(right child) or dp(curr) + 

        def dp(node, allow):
            if not node:
                return 0
            if (node, allow) in tracker:
                return tracker[(node, allow)]
            if not allow:
                ans = dp(node.left, True) + dp(node.right, True)
            else:
                ans = max(node.val + dp(node.left, False) + dp(node.right, False), dp(node.left, True) + dp(node.right, True))
            tracker[(node, allow)] = ans
            return ans

        return dp(root, True)
        