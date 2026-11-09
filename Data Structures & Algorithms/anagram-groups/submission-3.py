class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sorting adds a complexity of mlogm wher m is the length of the longest string
        #alphabets are limited by 26 characters
        anas = {}
        ans = []
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1 #tells us he releative offset from a and tell us what letter got ofset.
            der_key = tuple(freq)
            if der_key in anas:
                anas[der_key].append(s)
            else:
                anas[der_key] = [s]
        for t in anas:
            ans.append(anas[t])
        return ans
        

        