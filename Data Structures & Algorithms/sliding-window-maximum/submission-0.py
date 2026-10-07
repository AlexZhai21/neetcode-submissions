import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heep = []
        ans = []
        l = 0
        r = k - 1
        while r < len(nums):
            for i in range(l, r + 1):
                heapq.heappush(max_heep, -nums[i])
            ans.append(-heapq.heappop(max_heep))
            l += 1
            r += 1
            max_heep = []
        return ans




        