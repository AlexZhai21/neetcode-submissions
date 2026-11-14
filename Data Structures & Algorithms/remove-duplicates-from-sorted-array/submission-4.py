class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #o(n) time, o(1) space
        k = 1
        n = len(nums)
        if n == 1:
            return k
        l = 1 #l is the item to swap to next
        r = 1
        for r in range(1, n):
            # print(f"{r} is {curr}")
            # print(nums[r])
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
                k += 1
                
        
        
        return k
        
