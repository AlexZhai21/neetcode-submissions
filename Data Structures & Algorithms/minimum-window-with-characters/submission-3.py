class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        ans = ""
        #shrink the window when you have more than you need
        #when woudl shirnk:
        #1. when you have irrelevant letters (letters not in t_tracker)
        #2. when you have more of a letter than needed and your substring starts at that letter

        s_tracker = {}
        t_tracker = {}
        l = 0 #start of the answer substring
        for i in t:
            t_tracker[i] = 1 + t_tracker.get(i, 0)
        for r in range(len(s)):
            if s[r] in t_tracker: #this means this is part of the t substring
                s_tracker[s[r]] = 1 + s_tracker.get(s[r], 0)
                while l < r and ((s_tracker[s[r]] > t_tracker[s[r]] and s[l] == s[r]) or s[l] not in t_tracker or (s[l] in s_tracker and s_tracker[s[l]] > t_tracker[s[l]])): #when u get more than you need off s[l]/s[r] you can shrink if l starts there 
                    if s[l] in s_tracker:
                        s_tracker[s[l]] -= 1
                    l += 1 #after this, l should be the start of a new potential answer substring
    
         
            if (r - l + 1 < len(ans) or ans == "") and s_tracker.keys() == t_tracker.keys() and all(s_tracker[key] >= t_tracker[key] for key in t_tracker):
                curr_ans = ""
                for i in range(l, r + 1):
                    curr_ans += s[i]
                ans = curr_ans
            

        print(s_tracker)
        return ans
            

        