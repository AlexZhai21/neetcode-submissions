class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #o(n) time and o(1) space, since the tracker can ONLY BE UP TO SIZE 3 SINCE WE ONLY HAV 3 POSSIBLE VALUES
        tracker = {0:0, 1:0, 2:0 }
        for n in nums:
            tracker[n] = tracker.get(n, 0) + 1
        curr = 0
        for i in range(len(nums)):
    
            while tracker[curr] == 0:
                curr += 1
            nums[i] = curr
            tracker[curr] -= 1


