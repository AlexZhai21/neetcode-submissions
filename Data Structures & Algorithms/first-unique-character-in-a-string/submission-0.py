class Solution:
    def firstUniqChar(self, s: str) -> int:
        tracker = {}
        for i in s:
            tracker[i] = tracker.get(i, 0) + 1
        for i in range(len(s)):
            if tracker[s[i]] == 1:
                return i
        return -1