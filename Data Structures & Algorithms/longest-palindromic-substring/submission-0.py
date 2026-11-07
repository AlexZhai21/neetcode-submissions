from collections import deque
class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s) 
        ans = []
        for i in range(n):
            curr_ans = deque([s[i]])
            
            l = i -1
            r = i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    curr_ans.appendleft(s[l])
                    curr_ans.append(s[r])
                    l -= 1
                    r += 1
                else:
                    break
            if len(curr_ans) >= len(ans):
                ans = "".join(curr_ans)
        for i in range(n-1):
            curr_ans = deque([s[i], s[i + 1]])
            
            c1 = i
            c2 = i + 1
            if s[c1] != s[c2]:
                continue
            r = c2 +1
            l = c1 - 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    curr_ans.appendleft(s[l])
                    curr_ans.append(s[r])
                    l -= 1
                    r += 1
                else:
                    break
            if len(curr_ans) >= len(ans):
                ans = "".join(curr_ans)

        return ans
                




            

        
        