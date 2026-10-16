class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #COPYNG NEETCODES SOLUTION
        n, node = len(points), 0
        dist = [float('inf')] * n 
        visited = [False] * n
        edges, ans = 0,0
        while edges < n-1: #the reason is we just need to connect everything once, a minimum spanning tree
            visited[node] = True #visited the current node now and dont go back
            nextNode = -1 #not sure why yet
            for i in range(n):
                if visited[i]:
                    continue
                if not visited[i]:
                    currDist = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                    dist[i] = min(dist[i], currDist) #did we find a shortesr distance to node i?
                    if nextNode == -1 or dist[i] < dist[nextNode]: #if next Node is -1, that means we havent decided on a next node yet, IF WE HAVE DECIDED ON ON, BUT WE FIND SOMETHING THATS EVEN CLOSER THAN OUR DECIDED ONE, WE REPLACE IT
                        nextNode = i
            ans += dist[nextNode] #we move onto the next closest unseen node
            node = nextNode
            edges += 1
        return ans
        