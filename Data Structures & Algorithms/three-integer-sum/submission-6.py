from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
 
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l]+ nums[r] < target:
                    l += 1
                else:
                    if sorted([nums[i], nums[l], nums[r]]) not in ans:
                        ans.append([nums[i], nums[l], nums[r]])
                    l += 1
        

        return ans






        




        