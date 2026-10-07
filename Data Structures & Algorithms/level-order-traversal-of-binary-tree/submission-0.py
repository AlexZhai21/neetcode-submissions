# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        bfs = deque()
        if root is None:
            return ans
        bfs.append(root)
        ans.append([root.val])
        curr_level =[]
        curr_nodes = []
        while bfs:
            top_node = bfs.popleft()
            if top_node.left:
                curr_level.append(top_node.left.val)
                curr_nodes.append(top_node.left)
            if top_node.right:
                curr_level.append(top_node.right.val)
                curr_nodes.append(top_node.right)
            if len(bfs) == 0:
                bfs.extend(curr_nodes)
                curr_nodes = []
                if curr_level:
                    ans.append(curr_level)
                curr_level = []
        return ans
            


        