import heapq
from collections import deque
class Solution:
    def reorganizeString(self, s: str) -> str:
        tracker = {}
        ans = []
        maxHeap = []
        for i in s:
            tracker[i] = tracker.get(i, 0) - 1
        for t in tracker:
            heapq.heappush(maxHeap, [tracker[t], t])
        que = deque([])
        while maxHeap:
            top = heapq.heappop(maxHeap)
            ans.append(top[1])
            top[0] += 1
            if que and top[1] != que[0][1]:
                heapq.heappush(maxHeap, que.popleft())
            if top[0] < 0:
                que.append(top)
        if not que:
            return "".join(ans)
        return ""
        
        