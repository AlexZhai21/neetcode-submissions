# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.res = True
   
        def dfs(self, root):
            if root is None:
                return 0
            left_b = dfs(self, root.left) #dfs must return the heights ofthefolliwng subtrees    
            right_b = dfs(self, root.right)
            if abs(left_b - right_b) > 1:
                self.res = False
                return self.res
            return 1 + max(left_b, right_b)
        dfs(self = self, root = root)
        return self.res


            



        