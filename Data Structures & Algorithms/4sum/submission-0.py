class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        n = len(nums)
        for i in range(n-2): #o(n^3) time, o(n) space
            n_i = nums[i]
            for j in range(i + 1, n-1):
                n_j = nums[j]
                curr_sum = n_i + n_j
                t = target - curr_sum
                l = j + 1
                r = n-1
                while l < r:
                    two_sum = nums[l] + nums[r] 
                    if two_sum == t:
                        ans.add((n_i, n_j, nums[l], nums[r]))
                        # print(f"found! adding {n_i}, {n_j}, {nums[l]}, {nums[r]}, for a target sum of {t}")
                        l += 1
                        r -= 1
                    elif two_sum > t:
                        r -= 1
                    else:
                        l += 1
        to_return = []
        for i in ans:
            to_return.append(list(i))
        return to_return




        