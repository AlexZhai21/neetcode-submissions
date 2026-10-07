class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #returns true if within k + 1 numbers thers a duplicate
      
        l, r = 0, 0
        tracker = {}
        while r < len(nums):
            n = nums[r]
            if n in tracker: # we have seen this number before
                if r - tracker[n] <= k:
                    return True
                else:
                    tracker[n] = r
            elif n not in tracker: #this means that we haven't seen this number before
                tracker[n] = r
            r += 1
        return False

            
            
        