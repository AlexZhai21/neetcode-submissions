class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      ans = 0
      l = 0
      seen = set()
      for r in range(len(s)):
        while s[r] in seen: #this means the current letter we are on we've already seen and theres a duplciate in our substring:
          seen.remove(s[l])
          l += 1 #we shrinking our substring until the duplciate is removed
        seen.add(s[r])
        ans = max(ans, len(seen))
      return ans
