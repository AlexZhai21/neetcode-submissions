class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tracker = {} 
        n= len(nums)
        for i in nums:
            tracker[i] = tracker.get(i, 0) + 1
            if tracker[i] > n/2:
                return i



