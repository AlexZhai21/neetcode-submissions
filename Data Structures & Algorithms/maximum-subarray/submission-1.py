class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        tracker = {}
        len_n = len(nums)
        self.curr_max = float('-inf')

        def dp(i): #where i represents the maximum subarray stating from and using index i and curr_sum is where we are at for the sub r
            if i >= len_n: 
                return 0
            if i in tracker:
                return tracker[i]
            n = nums[i]
            ans = n + max(dp(i + 1), 0) #have to start off at 0 if we dont include it as part of the subarray cuz subarray gotta be continious
            #the reason i define the state as starting from AND USIGN index i was cuz if you define it as just starting form i, the logic can get really complex.
            #for example, for starting at index i, you can choose to ues index i or not choose to, but if you dont choose to, you cant return ans upwards since that would cause it to not be a subarray anymore.
            tracker[i] = ans
            if ans > self.curr_max:
                self.curr_max = ans
            return ans
        dp(0)
        return self.curr_max
        
        