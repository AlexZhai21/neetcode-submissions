# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(self, root_1, subroot):
            if not root_1 and not subroot:
                return True
            if root_1 and not subroot or subroot and not root_1:
                return False
            if root_1.val != subroot.val:
                return False 
            return isEqual(self, root_1.left, subroot.left) and isEqual(self, root_1.right, subroot.right)
        def dfs(self, root_1, subroot):
            if root_1 is None:
                return False
            if root_1.val == subroot.val:
                if isEqual(self, root_1, subroot):
                    return True
            return dfs(self, root_1.left, subroot) or dfs(self, root_1.right, subroot)
        return dfs(self, root, subRoot)
            

        