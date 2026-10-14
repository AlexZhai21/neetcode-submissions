class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tracker = {}
        s_len = len(s)
        p_len = len(p)

        def dp(i, j): #can we match the pattern using s[i:] and pattern p[j:]
            if (i, j) in tracker:
                return tracker[(i, j)]
            if i >= s_len and j >= p_len:
                return True
            if j >= p_len:
                return False
            if i >= s_len:
                if j < p_len - 1 and p[j + 1] == "*":
                    ans = dp(i, j + 2)
                else:
                    return False

            
            elif s[i] == p[j] or p[j] == ".": #pattern is equal: a a, a a*a, a ab
                if j < p_len - 1 and p[j + 1] == "*":
                    ans = dp(i + 1, j + 2) or dp(i + 1, j) or dp(i, j + 2) #can choose to use it and mveo on, use it and stay on current one, or dont even use it
                else:
                    ans = dp(i + 1, j + 1) #if the latter half doesnt have star, you HAVE to use it otherwise ur cooked
                    
            elif s[i] != p[j]:
                if j < p_len - 1 and p[j + 1] == "*": #can skip
                    ans = dp(i, j + 2)
                else:
                    ans = False

            tracker[(i, j)] = ans
            return ans
            
        return dp(0,0)


        