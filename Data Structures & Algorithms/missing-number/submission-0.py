class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = 0
        actual_sum = 0
        n = len(nums)
        for i in range(n + 1):
            expected_sum += i
        for n in nums:
            actual_sum += n
        if actual_sum == expected_sum:
            return 0
        else:
            return expected_sum - actual_sum
        