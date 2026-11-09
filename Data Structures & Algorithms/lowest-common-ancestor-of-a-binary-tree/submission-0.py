# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #not bfs sinece hat just tell syou the level but not what the parent is
        def childer(root):
            if not root:
                return 0
            r_v = root.val
            ans = 0
            if r_v == p.val or r_v == q.val: 
                ans += 1
            lc = childer(root.left)
            rc = childer(root.right)
            if type(lc) != int:
                return lc
            if type(rc) != int:
                return rc
            ans += lc
            ans += rc
            if ans >= 2:
                return root

            return ans
        return childer(root)
        