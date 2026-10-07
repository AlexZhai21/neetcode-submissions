class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles) #N 
        ans = r # this is a number that you can guarantee finishing the dicks within a certain time
        while l <= r:
            k = l + (r -l) // 2
    
            time = 0
            for b in piles:
                time += math.ceil(b/k) #number of hours needed to finish that pile
            if time <= h:
                ans = min(k, ans)
                r = k - 1
            elif time > h: #this means this rate is too slow
                l = k + 1
        return ans

        