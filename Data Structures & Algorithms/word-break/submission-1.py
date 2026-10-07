class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #dp[i] -> can you split it starting from here
        tracker = {} #should be like falses if u already found a situation to be false
        n = len(s) #number of words
        def dp(start, end):
            if (start, end) in tracker:
                return False
            the_string = s[start: end + 1]
            if the_string in wordDict and end == n -1:
                return True #this was the last thing and it is prat of it
            
            if the_string not in wordDict:
            
                return False
            for i in range(end + 1, n):
                if dp(end + 1, i):
                    return True
                else:
                    tracker[(end + 1, i)] = False
            return False
        for i in range(n):
            if dp(0, i):
                return True
        return False


        

#neetcode
#n, eetcode -> return false
#ne, etcode -> retrunf alse, ne alread isnt in it

#neetc, ode -> rturn false
        