# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_Height(root): #get the height of a tree with root node = root
            if root is None:
                return 0
            else:
                return 1 + max(get_Height(root.left), get_Height(root.right))
        
        def recur_path(root):
            return get_Height(root.left)+ get_Height(root.right)
        ans = 0
        tracker = deque()
        tracker.append(root)
        while len(tracker) > 0:
            top =tracker.popleft()
            ans= max(recur_path(top), ans)
            print(recur_path(top))
            if top.left:
                tracker.append(top.left)
            if top.right:
                tracker.append(top.right)
        return ans
      


    


        
        