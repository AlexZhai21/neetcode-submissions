import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        k_tracker = {}
        graph = {}
        ans = float('inf')
        for i in range(n):
            graph[i] = []
        for f in flights:
            graph[f[0]].append([f[2], f[1]]) #price, destination node
        minHeap = [[0, src, 0]] #total price, node, cities visited, can visit at most k + 1 cities
        heapq.heapify(minHeap)

        while minHeap:
            n = heapq.heappop(minHeap) #next node
            price = n[0]
            node = n[1]
            ks = n[2]
            if node not in k_tracker or ks < k_tracker[node]: #if never been to this node before (this is the cheapest way to reach it) or u found a cheaper way but this way is faster to reach, then add, otherwise, if its slower and uve been ther no point in
                k_tracker[node] = ks
            else:
                continue 
            if ks > k + 1:
                continue
            if node == dst:
                ans = min(ans, price)
                continue
             # this path didnt ercah desitnation within k stops (k + 1 flights)
            for i in graph[node]:
                i_price = i[0] #total price to go from node to i_node
                i_node = i[1]
                
                    #if its the first time going ot this new city or you can go to this city in less stops than the previous way you ercahed here (by dijkstras this cannot be cheaper than what we already saw)
                heapq.heappush(minHeap, [price + i_price, i_node, ks + 1])
   
        if ans != float("inf"):
            return ans
        return -1
  
            


        
        
        