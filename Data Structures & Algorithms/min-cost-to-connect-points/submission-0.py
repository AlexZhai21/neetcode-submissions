from collections import defaultdict
import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def dist_c(p1, p2):
            x1 = p1[0]
            x2 = p2[0]
            y1 = p1[1]
            y2 = p2[1]
            return abs(x1 - x2) + abs(y1 - y2)
        graph = defaultdict(list)
        minHeap = []
        ans = 0
        seen = set()

        for i in range(len(points)):
            p1 = points[i]
            for j in range(i + 1, len(points)):
                p2 = points[j]
                der_dist = dist_c(p1, p2) #distance between p1, p2
                graph[i].append([der_dist, j])
                graph[j].append([der_dist, i]) #creates graph between all the points
        
        for i in graph[0]:
            heapq.heappush(minHeap, i)
        seen.add(0)
        while minHeap:
            closest = heapq.heappop(minHeap) #closest is the shortest way we could hve ogtten to it
            der_p = closest[1]
            dist = closest[0]
            if der_p not in seen:
                ans += dist
                for i in graph[der_p]:
                    heapq.heappush(minHeap, i)
            seen.add(der_p)
        return ans



                #dijsktras -> the first time we pop something 



        
        
        