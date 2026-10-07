class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tracker = {}
        n = len(nums)
        def dp(i, s1, s2): #d_sum is desired diff
            if (i, s1, s2) in tracker:
                return tracker[(i, s1, s2)]
            if i == n:
                return s1 == s2

            #either include this as part of subset 1 or part of subset 2
            curr = nums[i]
            ans =  dp(i + 1, s1 + curr, s2) or dp(i + 1, s1, s2 + curr)
            tracker[(i, s1, s2)] = ans
            return ans
            #if part of subset 1:
            #can you partition subarray i + 1 to have like s2 and s1 have a difference of current number

        return dp(0,0,0)




            

        