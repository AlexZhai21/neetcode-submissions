#greedy
#O(n) time
class Solution:
    def jump(self, nums: List[int]) -> int:
        #first one is nonzero guaranteed
        #my idea: for each index, look at all possible jumps, jump to the max if the max can take u further than the furtherst current jump could be able to take you can otherwise if it cant jump to the furthest non zero jump
        #
        i = 0 #index we are at
        ans = 0
        end = len(nums) - 1
        while i != end:
            curr_j = nums[i]
            next_jump = (float('-inf'), float('-inf')) #index to jump to, jump "range" we can get through that index
            for j in range(1, curr_j + 1):
                next_index = i + j #this is the index we will be jumping to
                if next_index == end:
                    ans += 1
                    return ans
                # if next_index > end: #idt thsi should ever happen since u should be reaching equals to first
                #     break 
                if nums[next_index] + next_index > next_jump[-1] and nums[next_index] != 0: #next_jump[-1] is the furthest the curent oen can go
                    next_jump = (next_index, nums[next_index] + next_index)
            i = next_jump[0]
            ans += 1
        return ans
        

        

        #[5, 3, 1, 1, 2, 1,1, 4]
        