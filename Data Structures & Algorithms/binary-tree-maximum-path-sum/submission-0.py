# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.curr_ans = float("-inf")
        def recurpathsum(self, root): #this should return the max sum node and/or BRANCH from THIS ROOT, not the actual max sum path, since roots parent can only use one of the branches so you can't take both, the actual max sum path + the value we return would be different)
            if root is None:
                return 0
            left_sum = recurpathsum(self, root.left)
            right_sum = recurpathsum(self, root.right)
            to_return = root.val + max(0, left_sum, right_sum)
            path_ans = root.val
            if left_sum > 0:
                path_ans += left_sum
            if right_sum > 0:
                path_ans += right_sum
            if path_ans > self.curr_ans:
                self.curr_ans = path_ans
            return to_return
        recurpathsum(self, root)
        return self.curr_ans

            
        