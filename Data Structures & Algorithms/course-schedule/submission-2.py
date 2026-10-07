class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        pres = {}
        visitedPath = set()
        finished = set() #tracks what nodes you already know haeno cycle starting form ther
        for i in range(numCourses):
            graph[i] = []
            pres[i] = []
        for e in prerequisites:
            graph[e[1]].append(e[0])
            pres[e[0]].append(e[1]) #pres shows all the class you hav to take before this class, empty means no prereqs needed and is a good starting point
        def finish(node): #false if cycle, true if no cycle
            if node in visitedPath:
                return False
            if node in finished:
                return True
            visitedPath.add(node)
            for n in graph[node]:
                if not finish(n):
                    return False
            visitedPath.remove(node)
            finished.add(node)
            return True
      
        for r in graph:
            if r not in finished and not finish(r):
                return False
        return True

       
                


         
        