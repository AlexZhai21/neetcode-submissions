class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {}
        visited = set()
        for i in range(n):
            graph[i] = []
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1
        ans = 0
        for i in range(n):
            if i not in visited:
                ans += dfs(i)
        return ans
                

        

        