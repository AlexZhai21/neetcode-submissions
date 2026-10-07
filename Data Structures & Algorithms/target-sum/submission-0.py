class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tracker = {}
        n = len(nums)

        def dp(i, total):
            if (i, total) in tracker:
                return tracker[(i, total)]
            if i == n:
                return total == target
            curr_n = nums[i]

            ans = dp(i + 1, total + curr_n) + dp(i + 1, total - curr_n)
            tracker[(i, total)] = ans
            return ans
        return dp(0,0)


        