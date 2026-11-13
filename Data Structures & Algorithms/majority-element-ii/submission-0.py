class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        tracker = {}
        more_than = len(nums) //3 + 1
        ans = []
        for n in nums:
            tracker[n] = tracker.get(n, 0) + 1
            if tracker[n] == more_than:
                ans.append(n)
        return ans
        