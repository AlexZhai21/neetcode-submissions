import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        subbed = []
        ans = []
        for a in arr:
            heapq.heappush(subbed, [abs(a -x), a])
        for i in range(k):
            closest = heapq.heappop(subbed)
            ans.append(closest[1])
        return sorted(ans)
        