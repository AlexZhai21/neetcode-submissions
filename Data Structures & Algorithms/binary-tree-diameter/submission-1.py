# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dia(curr):
            if curr is None:
                return 0  
            right_path = dia(curr.right)
            left_path = dia(curr.left)
            self.ans = max(self.ans, right_path + left_path)
            return max(right_path + 1, left_path + 1)
        dia(root)
        return self.ans

            


        