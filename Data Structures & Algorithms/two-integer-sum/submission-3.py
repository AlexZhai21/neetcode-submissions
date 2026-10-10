class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #a + b = nums
        #a = nums - b
        tracker = {} #value: index
        for i in range(len(nums)):
            curr = nums[i]
            look_for = target - curr
            if look_for in tracker:
                return [tracker[look_for], i]
            tracker[curr] = i
        