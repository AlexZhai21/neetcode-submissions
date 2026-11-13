class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1 = 0 #p1 would be tracking what letter of t we are on
        len_t = len(t)
        len_s = len(s)
        p2 = 0 #p2 would be tracking what letter of s we are on, just need to check fi our p2 equals len of s
        if len_s > len_t:
            return False
        while p1 < len_t:
            if p2 == len_s:
                return True
            c_l = t[p1]
            if c_l == s[p2]:
                p2 += 1
            p1 += 1
        return p2 == len_s


        