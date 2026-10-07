class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for n in range(len(nums)):
            if target - nums[n] in tracker:
                return [tracker[target - nums[n]], n]
            tracker[nums[n]] = n





        #i + j = target
        #target - j = i
        