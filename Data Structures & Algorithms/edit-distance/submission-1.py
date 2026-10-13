class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        tracker = {}
        n1 = len(word1)
        n2 = len(word2)
        def dp(i, j): #index of word1, index of 
            if (i, j) in tracker:
                return tracker[(i, j)]
            if j >= n2 and i >= n1: #finished matching
                return 0
            elif i >= n1: #if i >= n u just have to keep inserting
                ans = 1 + dp(i, j + 1)
            elif j >= n2 and i < n1: #uve finished matching but still have shit in word 1
                ans = 1 + dp(i + 1, j) #keep deleting
            elif word1[i] == word2[j]: #ur prolly good
                ans = dp(i + 1, j + 1) 
            else:
                #delete = move i forward by oen and keep j
                #replace is you move forward both by 1 but you used an operation, insert is inserting right before i so you are still on the same one
                ans = 1 + min(dp(i + 1, j), dp(i + 1, j + 1), dp(i, j + 1))
            tracker[(i, j)] = ans
            return ans
        return dp(0,0)

        