class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tracker = {}
        n = len(nums)
        def dp(i, prev): #longest increasing subsequcen at nums[i:] can either add this one or dont
            if (i, prev) in tracker:
                return tracker[(i, prev)]
            if i >= n:
                return 0
            curr_n = nums[i]
            if curr_n > prev: #you can choose to incldue it or not include it
                ans = max(1 + dp(i + 1, curr_n), dp(i + 1, prev))
            if curr_n <= prev: #you cant even include it
                ans =  dp(i + 1, prev)
            tracker[(i, prev)] = ans
            return ans
        return dp(0, float('-inf'))
            

        