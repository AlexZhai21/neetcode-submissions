class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        graphs = {}
    
        for i in range(n):
            graphs[i] = []
        for e in edges:
            graphs[e[0]].append(e[1])
            graphs[e[1]].append(e[0])  
        if len(edges) != n - 1:
            return False
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for n in graphs[node]:
                dfs(n)
        
        dfs(0)
        if len(visited) != n:
            return False
        return True





        