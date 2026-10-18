import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        k_tracker = {}
        for i in range(n):
            graph[i] = []
        for f in flights: #O(E)
            from_i = f[0]
            to_i = f[1]
            price_i = f[2]
            graph[from_i].append([price_i, to_i])

        #k is the max number of stops, if you reach k stops and are NOT at destination airport, this is not the proper path, DON'T continue from here and add any of this neighbors to it

        #NUMBER OF FLIGHTS/PATHS - 1 = NUMBER OF STOPS
        minHeap = [[0, 0, src]] #price for starting point, num flights taken, city
        while minHeap: #O(ElogE)
            top = heapq.heappop(minHeap) #top thing
            t_price = top[0] #price to go from last reached node to dest
            t_flights = top[1]
            dest = top[2]
            if dest not in k_tracker:
                k_tracker[dest] = t_flights #ks reached, total price not needed to track since you know the first time you rach the city is the fastest you wille ver get there
            elif dest in k_tracker and t_flights < k_tracker[dest]: #this is a shorter way to reach it
                k_tracker[dest] = t_flights
            else:
                continue
            if t_flights >= k + 1 and dest != dst:
                continue
            elif t_flights <= k + 1 and dest == dst:
                return t_price
            elif t_flights < k + 1: 
                for i in graph[dest]:
                    to_push = [t_price + i[0], t_flights + 1, i[1]]
                    heapq.heappush(minHeap, to_push)
        return -1

        
        