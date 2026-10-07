class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        nus = len(nums)
        ans = [None] * nus
        zero_found = 0
        for n in nums:
            if n != 0:
                total_prod *= n
            else:
                zero_found += 1
        if zero_found  >1:
            for i in range(nus):
                ans[i] = 0
        else:
            for i in range(nus):
                
                if zero_found:
                    if nums[i] != 0:
                        ans[i] = 0
                    else:
                        ans[i] = total_prod
                else:
                    ans[i] = total_prod // nums[i]
        
        return ans

        
        
        