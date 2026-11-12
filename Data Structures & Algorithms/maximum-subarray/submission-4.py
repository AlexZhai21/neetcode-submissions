class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        tracker = {}
        def dp(i): #dp(i) = maximum subarray using a subarray starting from AND USING i
            if i >= n:
                return 0
            #at each index, you can choose to either include this one and continue your subarray or not include and start a new subarray
            #max(nums[i] + dp(i -1), dp(i - 1)) not allowed because if we did that, subarray starting form i-1 could include i-1 onwards but not i, which is then NOT a subarray
            #issue with slidign window is how do we decide when to start shrinkignt he window?
            if i in tracker:
                return tracker[i]
            use = max(nums[i] + dp(i + 1), nums[i])
            tracker[i] = use
            return use
        ans = float('-inf')
        for i in range(len(nums)):
            ans = max(ans, dp(i))

        return ans
            #either continue currnt subarray or start new subarray, only two options
            #continue current is simpel: nums[i] + dp(i+1)
            #start new would just be dp(i+1), but the issue is we cant return this upwards since index i-1 might use dp(i + 1) but not incldue the middle one

        