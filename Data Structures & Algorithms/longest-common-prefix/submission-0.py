class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        p = 0 #global pointer to tell su what letter we are on
        tracker = {}
        for s in strs:
            tracker[s] = len(s) #o(n*m), where n is the number of strings and m is the length of the longest sring
        ans = []
        while True: 
            last = None
            for s in strs:
                l_s = tracker[s] #the length
                if p >= l_s:
                    return "".join(ans) #since once one string is done iterating, impossible ot extend the prefix
                if not last:
                    last = s[p]
                else:
                    if s[p] != last:
                        return "".join(ans)
            
            ans.append(last)
            last = None
            p += 1
        return "".join(ans)
                
        