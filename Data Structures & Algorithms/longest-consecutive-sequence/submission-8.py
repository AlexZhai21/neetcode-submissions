class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        tracker = set() #knowing how many times a signle number appears is completley useless
        #the start of the sequence is a number, n, that doesnt have n-1 inside
        nums = set(nums)
        starts = []

        for n in nums:
            if n-1 not in nums:
                starts.append(n)
        ans = 0
        for i in starts:
            curr_ans = 0
            curr_num = i
            while curr_num in nums:
                curr_ans += 1
                curr_num += 1
            ans = max(curr_ans, ans)
        return ans


