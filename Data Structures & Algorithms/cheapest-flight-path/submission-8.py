from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Dijkstras timed out, try using BFS but limit of only k things to explore
        graph = {}
        k_tracker = {}
        ans = float('inf')
        for i in range(n):
            graph[i] = []
        for f in flights:
            fr_i = f[0]
            to_i = f[1]
            pr_i = f[2]
            graph[fr_i].append([to_i, pr_i]) #destination, price
        tracker = deque([[0, src, 0]]) # the level, the city we at, the price so far 
       
        while tracker:
            top = tracker.popleft() #top most thing
            level = top[0]
            city = top[1]
            price = top[2]
            if level >= k + 2:
                break
            if city not in k_tracker:
                k_tracker[city] = price #BFS IS OPPOSITE of the dijkstras one, first time you see it is guaranteed the shortest ks to reach it, but not necessasrily price
            elif city in k_tracker and price < k_tracker[city]: #this is a shorter way to reach it
                k_tracker[city] = price
            else:
                continue
            if city == dst:
                ans = min(ans, price)
            else:
                for j in graph[city]:
                    tracker.append([level + 1, j[0], price + j[1]])
        if ans == float('inf'):
            return -1
        return ans

    


        #flight paths - 1 = number of stops
        
        