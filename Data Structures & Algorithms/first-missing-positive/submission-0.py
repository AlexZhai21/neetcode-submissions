class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #we dont care about any of the negative numbers
        #smallest possible smallest poitive integer is 1
        #largest is n + 1
        
        n = len(nums)
        p = 0
        while p < n:
            curr = nums[p]
            if curr > n or curr <= 0:
                p += 1

            else:
                if nums[curr-1] != curr: #want to move this positive integer to its proper place
                    if curr -1 > p: #dont increment p forward
                        nums[curr-1], nums[p] = curr, nums[curr-1]
                    else:
                        nums[curr-1], nums[p] = curr, nums[curr-1] #assume that everything before p is ignorable
                        p +=1
                else:
                    p += 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

