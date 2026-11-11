class Solution:
    def minimumSteps(self, s: str) -> int:
        #0 is white, 1 is black
        p_sums = [0]
        for i in s:
            p_sums.append(int(i) + p_sums[-1])
        ans = 0
        for i in range(1, len(p_sums)):
            if s[i-1] == "0":
                ans += p_sums[i-1]
        return ans

