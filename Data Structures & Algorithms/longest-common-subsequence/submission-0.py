class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        tracker = {} 
        n1 = len(text1)
        n2 = len(text2)
        self.ans = 0

        def dp(i, j): #longest ccommon sequenec with text1 starting from i and text 2 starting from j      
            if (i, j) in tracker:
                return tracker[(i, j)]
            if i >= n1:
                return 0

            if j >= n2:
                return 0
            if text1[i] == text2[j]:
                ans = 1 + dp(i + 1, j + 1)
            else:
                ans =  max(dp(i, j + 1), dp(i + 1, j), dp(i + 1, j + 1)) 
            if ans > self.ans:
                self.ans = ans
            tracker[(i, j)] = ans
            return ans
        dp(0,0)
        return self.ans

            #dp[i] = 
        