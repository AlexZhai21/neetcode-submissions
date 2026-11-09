class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        tracker = {0: 1}
        pre_sum = 0
        for n in nums:
            pre_sum += n
           
            look_for = pre_sum - k
            ans += tracker.get(look_for, 0)
            tracker[pre_sum] = tracker.get(pre_sum, 0) + 1
        return ans

        