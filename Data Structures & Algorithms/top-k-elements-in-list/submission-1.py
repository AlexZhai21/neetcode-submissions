import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [None] * k
        heap_len = 0
        minHeap = []
        heapq.heapify(minHeap)
        tracker = {}
        for n in nums:
            tracker[n] = tracker.get(n, 0) + 1

        for t in tracker:
            heapq.heappush(minHeap, (tracker[t], t))
            heap_len += 1
            while heap_len > k:
                heapq.heappop(minHeap)
                heap_len -= 1
 
        for i in range(k):
            top = heapq.heappop(minHeap)
            ans[i] = top[1]
        return ans            


        