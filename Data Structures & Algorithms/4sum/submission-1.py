class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        for i in range(n-2): #o(n^3) time, o(n) space
            n_i = nums[i]
            if i > 0 and n_i == nums[i-1]:
                continue
            for j in range(i + 1, n-1):
                n_j = nums[j]
                if j > i + 1 and n_j == nums[j-1]:
                    continue
                curr_sum = n_i + n_j
                t = target - curr_sum
                l = j + 1
                r = n-1
                while l < r:
                    two_sum = nums[l] + nums[r] 
                    if two_sum == t:
                        ans.append([n_i, n_j, nums[l], nums[r]])
                        l += 1
                        # print(f"found! adding {n_i}, {n_j}, {nums[l]}, {nums[r]}, for a target sum of {t}")
                        while l <= r and nums[l] == nums[l -1]:
                            l += 1
                            
                    elif two_sum > t:
                        r -= 1
                        while r >= l and nums[r] == nums[r+1]: 
                            r -= 1
                    else:
                        l += 1
                        while l <= r and nums[l] == nums[l -1]:
                            l += 1
        return ans




        