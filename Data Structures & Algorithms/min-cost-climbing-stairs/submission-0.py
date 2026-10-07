class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        tracker = {}
        tracker[n] = 0 #to reach the end is 0 cost
        tracker[n - 1] = cost[n - 1]
        tracker[n - 2] = cost[n - 2]
        for i in range(n-3, -1, -1):
            tracker[i] = cost[i] + min(tracker[i +1], tracker[i + 2])
        return min(tracker[0], tracker[1])
        