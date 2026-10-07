from collections import deque
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = [None] * len(nums)
        ans = 0
        tracker = {}
        for i in range(len(nums)):
            if i > 0:
                prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            else:
                prefix_sum[i] = nums[i]
        for i in range(len(prefix_sum)):
            remainder = prefix_sum[i] % k
            if remainder == 0:
                ans += 1
            if remainder in tracker:
                ans += tracker[remainder]
            tracker[remainder] = tracker.get(remainder, 0) + 1
        return ans
            



        