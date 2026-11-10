class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tracker = {} #number: index
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            if curr not in tracker:
                tracker[curr] = i
            else:
                #this means curr is in tracker
                if i - tracker[curr] <= k:
                    return True
                tracker[curr] = i
        return False