class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        l,r = 0,0
        n = len(s)
        ans = 0
        while r < n:
            curr = s[r]
            while curr in window:
              
                window.remove(s[l])
                l += 1
            ans = max(ans, r - l + 1)
            window.add(curr)
            r += 1
        return ans 
        