# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validBST(self, root, greater_than, less_than):
           
            if root is None:
                return True
    
            # if root.right and root.right.val <= root.val or root.left and root.left.val >= root.val:
            #     return False
            if greater_than != None and root.val <= greater_than or less_than != None and root.val >= less_than:
                return False
            return validBST(self, root.left, greater_than = greater_than, less_than = root.val) and validBST(self, root.right, greater_than = root.val , less_than = less_than)
        return validBST(self, root = root.left, greater_than = None, less_than = root.val) and validBST(self, root = root.right, greater_than = root.val, less_than = None)

        