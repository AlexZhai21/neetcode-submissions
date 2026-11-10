class Solution:
    def rob(self, nums: List[int]) -> int:
        #bottom up
        n = len(nums)
        tracker = [0] * (n + 1) #tracker[i] = most amount of money you can rob starting from house i
        tracker[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            tracker[i] = max(nums[i] + tracker[i + 2], tracker[i + 1])
        return tracker[0] 