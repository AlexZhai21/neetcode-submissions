class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for i in nums:
            if i - 1 in nums:
                continue
            else: #this is the start of a subsequence 
                curr_ans = 1
                curr = i + 1
                while curr in nums:
                    curr_ans += 1
                    curr += 1
                ans = max(ans, curr_ans)
        return ans
