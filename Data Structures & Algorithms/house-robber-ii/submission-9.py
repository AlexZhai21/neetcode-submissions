class Solution:
    def rob(self, nums: List[int]) -> int:
        #two cases: rob from the 0th house or rob from the n-1th index house
        n = len(nums)
        if n == 1:
            return nums[0]
        tracker = {}
        def dp(i, end):
            if i >= end:
                return 0
            if i in tracker:
                return tracker[i]
            ans = max(nums[i] + dp(i + 2, end), dp(i + 1, end))
            tracker[i] = ans
            return ans
        first = dp(0, n-1)
        tracker = {}
        second = dp(1, n)
        return max(first, second)
        