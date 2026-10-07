class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = {}
        s2 = {}
        for thing in s:
            s1[thing] = 1 + s1.get(thing, 0)
        for thing in t:
            s2[thing] = 1 + s2.get(thing, 0)
        return s1 == s2

        