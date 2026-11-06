class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1]
        right_prod = [1]
        ans = []
        for i in range(len(nums) - 1):
            der_n = nums[i]
            left_prod.append(left_prod[-1] * der_n)
        for j in range(len(nums) - 1, 0, -1):
            der_n = nums[j]
            right_prod.append(right_prod[-1] * der_n)
        l_m = len(left_prod)
        for i in range(len(left_prod)):
            left_p = left_prod[i]
            right_p = right_prod[l_m - 1 - i]
            ans.append(left_p * right_p)
        return ans

        
        