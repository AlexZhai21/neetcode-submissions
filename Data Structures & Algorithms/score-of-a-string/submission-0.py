class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            score = abs(ord(s[i]) - ord(s[i - 1]))
            ans += score

        return ans


        