class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        end = len(s) - 1
        start = 0
        while start <= end:
            while not s[start].isalnum() and start < end:
                start += 1
            while not s[end].isalnum() and start < end:
                end -= 1
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True
            
        