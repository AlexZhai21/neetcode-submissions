class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        curr_window = {}
        p1, p2 = 0,0
        while p2 < len(s):
            curr_window[s[p2]] = curr_window.get(s[p2], 0) + 1
            while curr_window[s[p2]] > 1: #you have a duplicate:
                curr_window[s[p1]] -= 1
                if curr_window[s[p1]] == 0:
                    curr_window.pop(s[p1])
                p1 += 1
            ans = max(ans, len(curr_window))
            p2 += 1
        return ans
                

        