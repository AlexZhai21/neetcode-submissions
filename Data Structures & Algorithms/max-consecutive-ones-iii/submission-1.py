class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ks = k
        ans = 0
        l = 0
        r = 0
        n = len(nums)
        while r < n:
            curr = nums[r]
            while curr == 0 and ks <= 0:
                if nums[l] == 0:
                    ks += 1
                l += 1
            if curr == 0:
                ks -= 1
            ans = max(r - l + 1, ans)
            r += 1
        return ans

        