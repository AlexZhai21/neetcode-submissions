class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l+ ((r - l + 1) // 2)
            if nums[m] == target:
                ans = m
                return ans
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
                
            
        