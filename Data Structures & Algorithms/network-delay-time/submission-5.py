import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        seen = set()
        ans = 0
        for i in range(1, n + 1):
            graph[i] = []
        for t in times:
            ui = t[0]
            vi = t[1]
            ti = t[2]
            graph[ui].append([ti, vi])
        #keep track of the total time that has elasped so far (the most recent distance in seconds you traversed is how many seconds have elapsed)
        time_elapsed = 0
        minHeap = [(0,k)]
        while minHeap:
            next_node = heapq.heappop(minHeap)
            time = next_node[0]
            der_node = next_node[1]
            if der_node in seen:
                continue
            for i in graph[der_node]:
                heapq.heappush(minHeap, [time + i[0], i[1]])
            ans += time - time_elapsed
            time_elapsed = max(time_elapsed, time)
            seen.add(der_node)

        if len(seen) == n:
            return ans
        return -1
        




        
        