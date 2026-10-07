class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final = len(nums) - 1
        tracker = {}

        def dp(i): #index you are at, jump you do, return True if possible to reach the end from this index jumping j amount
            if i == final:
                return True
            if i in tracker:
                return tracker[i]
            j_amt = nums[i]
            if j_amt == 0:
                return False


            for jump in range(1, j_amt + 1):
                if dp(i + jump):
                    tracker[i] = True
                    return True
            tracker[i] = False
            return False
        return dp(0)

        