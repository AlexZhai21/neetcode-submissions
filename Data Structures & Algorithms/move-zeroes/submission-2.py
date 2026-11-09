class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        better way: track the LAST nonzero element
        """
        last = 0 #this is hte location of right after the last nonzero element, put the next thing here, our assumption is that last contains a zero element at nums[last]
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                continue
            
            else:
                temp = nums[last]
                nums[last] = nums[i]
                nums[i] = temp
                last += 1

        return nums