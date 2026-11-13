class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p_s = 0 #s pointer
        p_t = 0 #t pointer
        len_s = len(s)
        len_t = len(t)

        while p_s < len_s:
            if p_t == len_t:
                return 0 #this means t is aready a subsequence
            curr_let = s[p_s]
            if curr_let == t[p_t]:
                p_t += 1
            p_s += 1
        return len_t - p_t
        