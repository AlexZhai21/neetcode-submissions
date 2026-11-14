class Solution:
    def validPalindrome(self, s: str) -> bool:
        #issue with my origianl approach potentially: there might be a case where both enxt ones are valid, so which one to pick
        def checker(delet): #delete is 0 means make the decision from the left side situation
            n = len(s)
            l = 0
            r = n-1
            wrong = 1
            while l <= r:
                if s[l] != s[r]: #mismatch, try and see if any of the others can be deleted
                    if wrong <= 0:
                        return False
                    if not delet:
                        if s[l + 1] == s[r]:
                            l += 1
                            wrong -= 1
                        else:
                            return False
                    elif delet:
                        if s[r-1] == s[l]:
                            r-=1
                            wrong -= 1
                        else:
                            return False
                
                l += 1
                r -= 1
            return True
        return checker(0) or checker(1)       