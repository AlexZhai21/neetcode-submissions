# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs_equal(self, p_root, q_root):
            if p_root and not q_root or q_root and not p_root:
                return False
            if not q_root and not p_root:
                return True
            if p_root.val != q_root.val:
                return False
            l_equal = dfs_equal(self, p_root.left, q_root.left)
            r_equal = dfs_equal(self, p_root.right, q_root.right)
            return l_equal and r_equal
        return dfs_equal(self, p, q)


        