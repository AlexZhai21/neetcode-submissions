class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #o(1) space solution
        #index i ends up at (i + k)% n wher n is the length of nums
        #reverse
        n = len(nums)
        l = 0
        r = n-1
        def rev(l, r):
            while l <= r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r-= 1
            return
        rev(0, r)
        #after this, nums is reversed
        #k = how many vlaues on the "left side"
        rev(0, (k%n)-1)
        rev(k%n, n-1)

        