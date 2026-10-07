class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        tracker = {}

#buying and selling on the same day has no benefit..?  buyign and selling on the same day is the same as skipping
        def dp(i, buy): #buy is true if you can buy (dont hold any stock)
        #if you hold stock, buy is false 
            if i >= days:
                return 0
            if (i, buy) in tracker:
                return tracker[(i, buy)]
            curr_p = prices[i]
            if buy: #can either buy or buy and sell ont he same day
                ans = max(dp(i + 1, False) - curr_p, dp(i + 1, True))
            else: #have stock, cannot buy another, can sell or "sell and buy" whcih is hte same as moving forward
                ans = max(dp(i + 1, True) + curr_p, dp(i + 1, False))
            tracker[(i, buy)] = ans
            return ans
            
            

        return dp(0, True)


        