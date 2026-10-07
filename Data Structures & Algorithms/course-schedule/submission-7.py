class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        pre = {}
        global_v = set()
        for i in range(numCourses):
            graph[i] = []
            pre[i] = []

        for e in prerequisites:
            graph[e[1]].append(e[0]) #prereq -> course
            pre[e[0]].append(e[1]) #course -> prereqs
        
        def dfs(node, visited): # True if no cycle false if cycle
            if node in global_v:
                return
            if node in visited:
                return False
            visited.add(node)
            
            for i in graph[node]:
                if dfs(i, visited) == False:
                    return False
            visited.remove(node)
            global_v.add(node)
            return True
        num_roots = 0
    
        for i in pre:
            
            visited = set()
            if i not in global_v:
                if not dfs(i, visited):
                    return False
            global_v.add(i)
        return True
#graph:
#{1: 0, 0: 1}
        
       