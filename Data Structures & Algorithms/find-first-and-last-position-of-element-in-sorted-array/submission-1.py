class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) //2
            if nums[m] > target: #target is ont he left side
                r = m - 1
            elif nums[m] == target: #we found the target:
                start = m
                end = m
                while start -1 >= 0 and nums[start-1] == target:
                    start -= 1
                while end + 1 < len(nums) and nums[end + 1] == target:
                    end += 1
                

                return [start, end]
                     
            else:
                l = m + 1
        
        return [-1, -1]



        