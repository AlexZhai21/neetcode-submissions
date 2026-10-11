class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0,0
        ans = 0
        curr_zeros = 0
        while r < len(nums):
            
            if nums[r] == 0:
                curr_zeros += 1
            while curr_zeros > k:
                if nums[l] == 0:
                    curr_zeros -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
            

        return ans

        