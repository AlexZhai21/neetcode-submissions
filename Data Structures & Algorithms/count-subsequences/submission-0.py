class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n_s = len(s)
        n_t = len(t)
        tracker = {}

        def dp(i, j):
            if j >= n_t:
                return 1
            if i >= n_s:
                return 0
            if (i, j) in tracker: #number of ways to make t[j:] using s[i:]
                return tracker[(i, j)]

            if s[i] == t[j]:
                ans = dp(i + 1, j + 1) + dp(i + 1, j) #you can iether use it, but there might be another one that matches so you dont have to use it
            else:
                ans = dp(i + 1, j)
            tracker[(i, j)] = ans
            return ans
        return dp(0,0)