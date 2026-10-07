class Solution:
    def climbStairs(self, n: int) -> int:
        tracker = {} #tracker from step number to # of ways to get to the goal step from that step number
        tracker[n] = 1
        tracker[n - 1] = 1
        for i in range(n-2, -1, -1):
            tracker[i] = tracker[i + 1] + tracker[i + 2]
        return tracker[0]



        