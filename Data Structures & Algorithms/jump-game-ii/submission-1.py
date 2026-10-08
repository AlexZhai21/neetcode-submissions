#dynamic programming
class Solution:
    def jump(self, nums: List[int]) -> int:
        end = len(nums) - 1
        tracker = {}

        def dp(i): #number of jumps needed to reach the end
            if i == end:
                return 0
            if i > end:
                return float('inf') #impossible
            if i in tracker:
                return tracker[i]
            j_amt = nums[i] #how many jumps we can jumpm from position i
            ans = 1 + min([dp(i + j) for j in range(1, j_amt + 1)] + [float('inf')])
            tracker[i] = ans
            return ans
        return dp(0)




            

        