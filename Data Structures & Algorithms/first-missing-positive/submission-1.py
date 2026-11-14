class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #answer must be between 1 and n + 1
        n = len(nums)
        seen = set()
        for nu in nums:
            if nu > 0 and nu not in seen:
                seen.add(nu)
        for i in range(1,n + 2):
            if i not in seen:
                return i
        