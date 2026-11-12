class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #the logic here is that once your current window sum becomes negative, no matter whats ahead, keeping thi is objectivly worse for you (if its the best you would have saved it already, if everythignelse is psotive then keepingthis engative sum is bad, so just remove it)
        curr_sum = 0
        ans = float('-inf')
        for i in nums:
            curr_sum += i
            ans = max(ans, curr_sum)
            if curr_sum < 0:
                curr_sum = 0
        return ans        