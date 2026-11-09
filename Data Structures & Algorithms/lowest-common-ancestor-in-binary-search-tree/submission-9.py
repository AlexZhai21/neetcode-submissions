# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #curr node:
        #if p and q are both on the same side of the bst (either both elft or boht right), lowest common is below
        #if one is on oneside and one is ont he other side, curr node has to be the lca
        #if curr node is equiavlent to p or q, then curr is the lca
        p_v = p.val
        q_v = q.val
        def lca(root):
            if not root:
                return
            v = root.val
            if p_v < v and q_v > v or p_v > v and q_v < v or p_v == v or q_v == v:
                return root
            if p_v < v and q_v < v:
                return lca(root.left)
            if p_v > v and q_v > v:
                return lca(root.right)
        return lca(root)
            
        