class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i in range(len(nums)):
            if target - nums[i] in tracker:
                return [tracker[target - nums[i]], i]
            else:
                tracker[nums[i]] = i

        