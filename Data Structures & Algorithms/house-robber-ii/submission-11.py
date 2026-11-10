class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        tracker = [0] * (n + 1) #using the last one
        tracker[n-1] = nums[n-1] #initially using the first one, so cant use 0th case
        for i in range(n-2, 0, -1): #cant use first one since this one we consider the last one
            tracker[i] = max(nums[i] + tracker[i + 2], tracker[i + 1])
        print(tracker)
        
        use_last = tracker[1]
        tracker = [0] * (n + 1)
        tracker[n-2] = nums[n-2]
        for i in range(n -3, -1, -1):
            tracker[i] = max(nums[i] + tracker[i + 2], tracker[i + 1])
        print(tracker)
        use_first = tracker[0]
        return max(use_last, use_first)

        