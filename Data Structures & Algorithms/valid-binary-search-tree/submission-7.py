# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, greater, less): #greater gives us  what value node.val shoudl be greeater than, less gives us what value node.val should be less than
            if not node:
                return True
            if node.val <= greater or node.val >= less:
                return False
            return valid(node.left, greater, min(node.val, less)) and valid(node.right, max(node.val, greater), less)

        return valid(root, float('-inf'), float('inf'))