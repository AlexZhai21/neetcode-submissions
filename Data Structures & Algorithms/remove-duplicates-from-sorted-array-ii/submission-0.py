class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 1 #where to put other element
        seen = 1 #how many of each thign we have seen so far
        r = 1 #fast pointer

        while r < n:
            if nums[r] == nums[r-1]:
                if seen < 2:
                    nums[l] = nums[r]
                    l += 1
                    seen += 1
            else: 
                seen = 1
                nums[l] = nums[r]
                l += 1
            r += 1
        return l

        