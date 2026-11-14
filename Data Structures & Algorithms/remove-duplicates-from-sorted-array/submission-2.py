class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        l = 0
        r =0
        n = len(nums)
        while r < n:
            if nums[r]!= nums[l]: #
                l = r
                k += 1
            elif r != l:
                nums[r] = 101 #a number that istn possible
            r += 1
        removed = 0
        for i in range(n):
            if nums[i - removed] == 101:
                nums.pop(i - removed)
                removed += 1
        return k
        
