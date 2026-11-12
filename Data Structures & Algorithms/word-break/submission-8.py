class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        n = len(s)
        m = len(wordDict)
        tracker = {} #o(n * n * n)
        def dp(i, j, k): #i is a place where you put a space and seperate, j is what word in wordDict you are looking at, k = what index of wordDict[j] we are looking at 
            if i >= n and k >= len(wordDict[j]):
                return True
            if i >=n and k < len(wordDict[j]):
                return False
            if (i, j, k) in tracker:
                return tracker[(i, j, k)]
            ans = False
            if k >= len(wordDict[j]):
                #this is good it means we finished the current word
                for z in range(m):
                    ans |= dp(i, z, 0)
            else:
                c = s[i] #current letter c
                wd_w = wordDict[j][k]
                if c != wd_w: #if not equal, then this part of the string cannot be seperated into soemthign in word dict so end it right away
                    return False
                else: #that means we can potentially continue this word
                    ans |= dp(i + 1, j, k + 1)
            tracker[(i, j, k)] = ans
            return ans
        for j in range(len(wordSet)):
            if dp(0, j, 0):
                return True
        return False


            

        