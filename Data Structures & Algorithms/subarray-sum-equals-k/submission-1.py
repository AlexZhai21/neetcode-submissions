class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix_sums = {0: 1}
        p2 = 0
        curr_sum = 0
        while p2 < len(nums):
            curr_sum += nums[p2] #this is the current sum of the subarray from 0 to p2
            to_find = curr_sum - k
            ans += prefix_sums.get(to_find, 0)
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1
            p2 += 1
        return ans

