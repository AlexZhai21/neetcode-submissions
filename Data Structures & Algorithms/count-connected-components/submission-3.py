class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        ans = 0
        for i in range(n):
            graph[i] = []
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
    
        #this constructs the adjacency list
        visited = set() #tells us what nodes have been visited already
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
      
            for neighbor in graph[node]: #adjacnecy list has all the nodes conencted to this node
                dfs(neighbor)
            return 
        for n in graph:
            if n not in visited:
                dfs(n)
                ans += 1
        return ans
            

            
                
                