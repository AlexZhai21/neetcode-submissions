class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l <= r:
            m = l + (r-l)//2 #rate
            h_needed = 0
            for i in piles:
                h_needed += (i + m - 1) // m
            if h_needed > h:
                l = m + 1
            else:
                ans = m
                r = m - 1
        return ans
            



        