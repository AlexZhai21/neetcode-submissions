# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.to_return = float('-inf')
        def dfs(root):
            if not root:
                return 0
            left_path = dfs(root.left)
            # print(f"left_path at {root.val} is {left_path}")
            right_path = dfs(root.right)
            # print(f"right_path at {root.val} is {right_path}")
            ans = max(root.val, root.val + left_path, root.val + right_path, root.val + left_path + right_path)
            self.to_return = max(self.to_return, ans)
            # print(f"max at {root.val} is {ans}")
            return max(root.val, root.val+left_path, root.val + right_path)
        dfs(root)
        return self.to_return

        #return value should be the maximum paths um of the tree with root = root

        