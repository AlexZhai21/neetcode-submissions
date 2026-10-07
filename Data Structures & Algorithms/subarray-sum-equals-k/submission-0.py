class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [None] * len(nums)
        tracker = {}
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                prefix_sum[i] = nums[i]
            else:
                prefix_sum[i] = prefix_sum[i - 1] + nums[i]

        # #after this, prefix_sum should be done
        for i in range(len(prefix_sum)):
            curr_sum = prefix_sum[i]
            #three possibilities: curr sum too large (find a value )

            if curr_sum == k:
                ans += 1
            look_for = curr_sum - k
            if look_for in tracker:
                ans += tracker[look_for]
            tracker[curr_sum] = tracker.get(curr_sum, 0) + 1
        return ans


#curr_sum - old_sum == k
#curr_sum - k == old_sum

        