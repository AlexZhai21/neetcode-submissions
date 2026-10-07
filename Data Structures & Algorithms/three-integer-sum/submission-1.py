from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # tracker = defaultdict(list)
        # sorted_nums = nums.sort()
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         twosum = nums[i] + nums[j]
        #         tracker[twosum].append([i, j]) 
        # #After this double loop, tracker contains all the possible sums of 2 values + the 2 index that make up that sum

        # for twosum in tracker:
        #     for third in range(len(nums)):
        #         if twosum + nums[third] == 0:
        #             for pos_ans in tracker[twosum]:
        #                 if third not in pos_ans:
        #                     # new_ans = pos_ans.append(third) #The return value of append is None
        #                     new_ans = [nums[pos_ans[0]], nums[pos_ans[1]], nums[third]]
        #                     if sorted(new_ans) not in ans:
        #                         ans.append(new_ans)
        # #Need to deduplicate the list
        # return ans

        ans = []
        sorted_nums = nums.sort() 
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
                    r -= 1

        return ans






        




        