class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tracker = {}
        for i in range(len(nums)):
            n = nums[i]
            if n in tracker and i - tracker[n] <= k:
                return True
            tracker[n] = i
        return False
        