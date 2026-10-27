import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = []
        for s in stones:
            heapq.heappush(minHeap, -1 * s)

        while len(minHeap) > 1:
            x = -1 * heapq.heappop(minHeap)
            y = -1 * heapq.heappop(minHeap)
            if x == y:
                continue
            elif y < x:
                x = -1 * (x-y)
                heapq.heappush(minHeap, x)
        if minHeap:
            return -1 * minHeap[0]
        else:
            return 0