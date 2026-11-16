# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tracker = {}

        def equal(r, sr):
            if not r and not sr:
                return True
            #every single time you find soemthign that not equal, you have to restart the search again
            elif not sr and r:
                return False
            elif not r and sr:
                return False
            if (r, sr) in tracker:
                return tracker[(r, sr)]

            if r.val == sr.val:
                ans = (equal(r.left, sr.left) and equal(r.right, sr.right)) or equal(r.left, subRoot) or equal(r.right, subRoot)
            else:
                ans = equal(r.left, subRoot) or equal(r.right, subRoot)
            tracker[(r, sr)] = ans
            return ans
        return equal(root, subRoot)
        