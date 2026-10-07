class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n #index 0 should be product of everything up to index 0 but not icnluding index 0 in nums
        suffix = [1] *n #index j should be the product of everything after but not including index j
        ans = [1] * n
        for i in range(n-1):
            prefix[i + 1] = prefix[i] * nums[i]
        for i in range(1, n):
            suffix[n - i - 1] = suffix[n - i] * nums[n - i]
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        return ans
 
        
        