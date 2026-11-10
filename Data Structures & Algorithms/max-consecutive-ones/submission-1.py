class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        r = 0
        l = -1
        ans = 0
        n = len(nums)
        while r < n:
            curr = nums[r]
            if curr == 0:
                l = r

            ans = max(r - l, ans)
            r += 1
        return ans
        