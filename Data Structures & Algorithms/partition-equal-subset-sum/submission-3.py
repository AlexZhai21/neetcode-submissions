class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tracker = {}
        n = len(nums)
        if sum(nums) %2 != 0:
            return False
        def dp(i, curr_sum):
            if curr_sum < 0:
                return False
            if (i, curr_sum) in tracker:
                return tracker[(i, curr_sum)]
            
            if i == n:
                return curr_sum == 0
            curr_n = nums[i]
            a1 = dp(i + 1, curr_sum - curr_n) or dp(i + 1, curr_sum)
            tracker[(i, curr_sum)] = a1
            return a1
           
        return dp(0, sum(nums) // 2)


        
        