class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #n^2 constant time solution
        for i in range(1, len(nums)):
            curr = i
            prev = i -1
            while prev >= 0 and nums[curr] < nums[prev]:
                temp = nums[curr]
                nums[curr] = nums[prev]
                nums[prev] = temp
                curr = prev
                prev -= 1
        
        