class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tracker = {}
        ans = -1
        n_coins = len(coins)
    
        def dp(i,n): #i is the index of the coin we are using, n is the remaining amoutn elft      
            #either use the same coin or stop and start using the next coin
            if (i, n) in tracker:
                return tracker[(i, n)]
            if n == 0:
                return 0
            if n < 0:
                return float('inf') #this one is impossible
            
            same = 1 + dp(i, n-coins[i])
            next_c = float('inf')
            if i < n_coins - 1:

                next_c = dp(i + 1, n)
            tracker[(i, n)] = min(tracker.get((i, n), float('inf')), min(same, next_c))
            return tracker[(i, n)]
        ans = dp(0, amount)
        if ans != float('inf'): 
            return ans
        return -1
            
            
        