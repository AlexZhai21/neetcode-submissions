# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #inorder traversal of a valid bst gives us a sorted list
        inorder_l = []
        def inorder(node):
            if not node:
                return 
            left = inorder(node.left)
            inorder_l.append(node.val)
            right = inorder(node.right)
        
        inorder(root)
        for i in range(1, len(inorder_l)):
            if inorder_l[i] <= inorder_l[i-1]:
                return False
        return True