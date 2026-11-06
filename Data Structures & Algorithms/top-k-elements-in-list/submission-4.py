import heapq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tracker = defaultdict(int)
        minHeap = []
        ans = []
        for n in nums:
            tracker[n] += 1
        for t in tracker:
            heapq.heappush(minHeap, (tracker[t], t))
            while len(minHeap) > k:
                heapq.heappop(minHeap)
        for i in minHeap:
            ans.append(i[1])
        return ans
        

        