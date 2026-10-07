"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        tracker = {} #actual node to cloned node
        def cloner(top_node):
            if top_node in tracker:
                clone_node = tracker[top_node]
                return clone_node
            else:
                clone_node =Node(val =top_node.val)
                tracker[top_node] =clone_node
            n_list= []
            for i in top_node.neighbors:
                n_list.append(cloner(i))
            clone_node.neighbors=n_list
            return clone_node
        if node:
            return cloner(node)
        return None

