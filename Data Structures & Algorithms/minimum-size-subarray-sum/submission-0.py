class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        curr_sum = 0
        ans = float('inf')
        n = len(nums)
        while r < n:
            curr_sum += nums[r]
            while curr_sum >= target:
                ans = min(ans, r - l + 1)
                curr_sum -= nums[l]
                l += 1
            r += 1
            


        if ans == float('inf'):
            return 0
        else:
            return ans
        