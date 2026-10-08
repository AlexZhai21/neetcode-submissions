class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() #leas
        s.sort()
        ans = 0
        kid = 0
        num_kids = len(g)
        for i in range(len(s)):
            if kid >= num_kids:
                break
            c_size = s[i] #the size of the cookie
            if c_size >= g[kid]:
                
                kid += 1
        
                ans += 1
            
        return ans

        