class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = {}
        
        n = len(edges)
        parents = [None] * n
        for i in range(n):
            parents[i] = i #everything needs to be shifted up by one
        def find(x): #finds what gorup x belongs to:
            if parents[x] != x:
                return find(parents[x])
            return x
        def union(x, y): #union together 2 nodes to be in one group
            parents[find(y)] = parents[find(x)] #y now belogns in the same group as x
        for e in edges:
            x = e[0] - 1
            y = e[1] - 1
            p_x = find(x)
            p_y = find(y)
            if p_x == p_y: #these are alread in a group and have already been connected
                #cycle detected
                #the group they are in is p_x
                for i in range(n - 1):
                    e = edges[-1 - i]
                    if find(e[0] - 1) == p_x and find(e[1] - 1) == p_y: #this means that the 2 things in this edge are in the same group as the gorup wiht the cycle:
                        return [e[0], e[1]]

            else:
                union(x, y)
        
        # self.the_repeat = None
        # cycle_edges = set()
        
        
        
        
        
        
        
        
        
        # for e in edges:
        #     graph[e[0]] = graph.get(e[0], []) + [e[1]]
        #     graph[e[1]] = graph.get(e[1], []) + [e[0]]
        # visited = set()
        # def cycle_det(prev, node): #returns true if a cycle is detected, otherwise, return false
        #     if node in visited and node != prev:
        #         #the edge in the cycle is [min(prev, node), max(prev, node)]
        #         self.the_repeat = node
        #         cycle_edges.add((min(prev, node), max(prev, node)))
        #         return True #this means u visited a node again that WASNT just the node that we came from
        #     visited.add(node)
        #     for n in graph[node]:
        #         if cycle_det(prev = node, node = n):
        #             if self.the_repeat and (prev == self.the_repeat or node == self.the_repeat):
        #                 return False
        #             else:
        #                 cycle_edges.add((min(prev, node), max(prev, node)))
        #                 return True
        #             return True
        #     return False
        # cycle_det(None, 1)
        # return cycle_edges




        # # in_degrees = {}
        # # for e in edges:
        # #     in_degrees[e[0]] = in_degrees.get(e[0], 0) + 1
        # #     in_degrees[e[1]] = in_degrees.get(e[1], 0) + 1
        # # curr_ans = [None, None]
        # # for e in edges:
        # #     if in_degrees[e[0]] > 1 and in_degrees[e[1]] > 1:
        # #         curr_ans = [e[0], e[1]]
        # # return curr_ans


        