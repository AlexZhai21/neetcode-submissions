class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        tracker = {}
        
        def dp(x, y): #start off at 0,0
            if (x, y) in tracker:
                return tracker[(x, y)]
            if x >= m or y >= n:
                return 0
            if x == m-1 and y == n-1:
                return 1
            ans = dp(x + 1, y) + dp(x, y + 1)
            tracker[(x, y)] = ans
            return ans



        return dp(0,0)
        