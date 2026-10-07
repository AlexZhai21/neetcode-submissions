from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        in_edges = {}
        pres = {}
        tracker = deque()
        ans = []
        for i in range(numCourses):
            graph[i] = []
            pres[i] = []
        for e in prerequisites:
            graph[e[0]].append(e[1]) # courses -> prereqs (technically like incoming edges)
            pres[e[1]].append(e[0]) #prereqs -> courses, when we pop a prereq, we can remove -1 to all the incoming edge for each coures in courses
        for i in range(numCourses):
            in_edges[i] = len(graph[i])
            if len(graph[i]) == 0: #this is a root coures with no prereqs
                tracker.append(i) #after this, we get all the courese with no prereqs

        while tracker:
            curr_node = tracker.popleft() #takes the first 
            ans.append(curr_node)
            for c in pres[curr_node]: #all the ocurses that had this course as a prereq
                in_edges[c] -= 1
                if in_edges[c] == 0:
                    tracker.append(c)
        if len(ans) == numCourses:
            return ans
        else:
            return []
                    
            