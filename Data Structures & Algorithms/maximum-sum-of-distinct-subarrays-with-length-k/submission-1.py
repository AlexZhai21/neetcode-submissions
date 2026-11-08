class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        l, r = 0,0
        window = set()
        n = len(nums)
        ans = 0
        curr_ans = 0
        while r < n:
            der_n = nums[r]
            # print(window)
            while der_n in window or len(window) >= k:
                window.remove(nums[l])
                curr_ans -= nums[l]
                l += 1
            window.add(der_n)
            curr_ans += der_n
            if len(window) == k:
                ans = max(curr_ans, ans)
            r += 1
        return ans
