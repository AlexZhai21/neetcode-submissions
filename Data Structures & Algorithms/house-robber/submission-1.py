class Solution:
    def rob(self, nums: List[int]) -> int:
        tracker = {}
        n = len(nums)
        def dp(i):
            if i >= n:
                return 0
            if i in tracker:
                return tracker[i]
            ans = max(nums[i] + dp(i + 2), dp(i + 1)) #either rob this house and cant rob the next one or skip
            tracker[i] = ans
            return ans
        return dp(0) 

        