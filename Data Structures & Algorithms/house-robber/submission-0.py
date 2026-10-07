class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i] = max(dp[i + 2], dp[i + 3])
        ans = 0
        n = len(nums)
        tracker = {}
        tracker[n] = 0
        tracker[n - 1] = nums[n -1]
        tracker[n - 2] = nums[n -2]
        for i in range(n -3, -1, -1):
            tracker[i] = nums[i] + max(tracker[i + 2], tracker[i + 3])

        ans = max(tracker[0], tracker[1])
        return ans



        