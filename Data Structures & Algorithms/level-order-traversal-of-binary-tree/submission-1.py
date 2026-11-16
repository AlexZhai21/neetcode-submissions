# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([])
        ans = []
        if root:
            q.append(root)
        while q:
            n = len(q)
            curr_ans = []
            for i in range(n):
                top = q.popleft()
                curr_ans.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
            ans.append(curr_ans)
            curr_ans = []
        return ans

        