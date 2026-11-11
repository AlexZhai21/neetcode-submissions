class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        starts = []
        for n in nums:
            if n-1 not in nums:
                starts.append(n)
        ans = 0
        for s in starts:
            curr_ans = 0
            curr_num = s
            while curr_num in nums:
                curr_ans += 1
                curr_num += 1
            ans = max(ans, curr_ans)
        return ans

