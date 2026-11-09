class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            n = nums[i]
            if n == 0:
                continue
            
            else:
                j = i - 1
                k = i
                while j >= 0 and nums[j] == 0:
                    temp = nums[k]
                    nums[k] = nums[j]
                    nums[j] = temp
                    k -= 1
                    j -= 1
        return nums



        