class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #neetcodes solution
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            curr = abs(nums[i])
            if curr >= 1 and curr <= n: #potential solution but not including n + 1 since we dont have room for it              
                if nums[curr-1] == 0: #ither was a engative before, was 0 before, or we have a duplciate
                    nums[curr -1] = -1 * curr
                elif nums[curr -1] < 0:
                    continue
                else:
                    nums[curr-1] = -1 * nums[curr - 1]
        for i in range(n):
            if nums[i] >= 0:
                return i + 1
        return n +1
                
                

        