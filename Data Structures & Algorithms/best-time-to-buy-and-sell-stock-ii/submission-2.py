class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        #each day you can either buy, do nothing (buy and sell), sell, or sell and buy (do nothing), depending on what you have
        #my first intuition is that greedy shouldn't really be working since you need a globally opitmal thing, but i think BECAUSE we can buy and sell on the same day (or sell and buy on thesame day), we are never locked into a decision, so if we buy on a day and on a future day we realize tthat its betterto sell, we can sell an ten buy on the future day so its as if nothing happened
        #false if not
        buy = True
        curr_stock = 0 #price we bought the stock at
        for i in range(len(prices) - 1):
            curr_p = prices[i]
            next_p = prices[i + 1]
            if next_p > curr_p: #should sell at this
                if buy: #we dont have any stock yet
                    profit += (next_p - curr_p) #buy current day and sell immedietly so tnohgine sel changes
                else: #we have stock
                    profit += next_p #sell our stock for this price
                    buy = True
            else: #next_p <= curr_p, should buy tomorrow so sell whatever we have if we have anything
                if buy: #no stock
                    profit -= next_p #buy it
                    buy = False
                else: #we have stock, sell our stock to buy this cheaper one
                    profit += (curr_p - next_p)
        if not buy: #this means we just bought the lkast thign which is pointless
            profit += prices[-1]
        return profit
#logic: if you can buy cheaper, just buy
#if you can sell for profit, just sell. reason is that if you realize a day after you can get it for cheaper, you can just buy it again and then sell it again 

            


        