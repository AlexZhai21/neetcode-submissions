class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = {}
        l, r = 0,0
        n = len(nums)
        curr_ans = 0
        ans = 0
        while r < n:
            der_n = nums[r]
            while der_n in window and window[der_n] >= k:
                window[nums[l]] -= 1
                curr_ans -= 1
                l += 1
            window[der_n] = window.get(der_n, 0) + 1
            curr_ans += 1
            ans = max(ans, curr_ans)
            r +=1
        return ans