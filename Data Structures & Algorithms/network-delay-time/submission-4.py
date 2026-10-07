import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}

        visited = set()
        ans = -1
        minHeap = [[0, k, 0]] #time takes to reach source, source node, time (level)
        for i in range(n):
            graph[i + 1] = []
        for t in times:
            graph[t[0]].append([t[1], t[2]])
        heapq.heapify(minHeap)
        while minHeap: #in dickstras, the first time you pop it is guaranteed the fastest you can reach this
            top_t = heapq.heappop(minHeap) #top node (shortest time + node) 
            top_time = top_t[0]
            top_node = top_t[1]
            curr_level = top_t[2]
            
            if top_node in visited:
                continue
            visited.add(top_node)
            ans = max(ans, top_time)
            for i in graph[top_node]:
                n_node = i[0]
                n_time = i[1]
                heapq.heappush(minHeap, (n_time + top_time, n_node, curr_level + 1))
 
        if len(visited) == n:


            return ans
        return -1
    



        




        