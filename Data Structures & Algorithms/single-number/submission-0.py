class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #o(n) space
        tracker = {}
        for i in nums:
            tracker[i] = tracker.get(i, 0) + 1
        for t in tracker:
            if tracker[t] < 2:
                return t

        
        