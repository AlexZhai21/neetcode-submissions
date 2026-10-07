class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        tracker = {} #max profit you can get starting from day i if prev deicsion was sell (0 or 1)
        total = len(prices)

        def dp(i, sell, c): #i is the day we are on, sell = 1 if sold, c is the worth of the coin on hand, c = -1 if no coino n hand
        #i -> profit given you buy on day i, sell on day i, or do nothing on day i
            if (i, sell, c) in tracker:
                return tracker[(i, sell, c)]
            if i >= total:
                return 0

            curr_p = prices[i]
            if sell == 1: #
                ans = dp(i + 1, 0, -1) #after selling prev day, you can't buy on day i so have to move on
            elif c >= 0: #if you ahve a coin, you cant buy but you can sell
                ans = max(dp(i + 1, 1, -1) + curr_p, dp(i + 1, 0, 1))
            # ans = max(dp(i + 1, 1) + curr_p, dp(i + 1, 0) - curr_p, dp(i + 1, 0))
            else: #no coin on hand, cant sell but can buy
                ans = max(dp(i + 1, 0, 1) - curr_p, dp(i + 1, 0, -1))
            tracker[(i, sell, c)] = ans

            return ans
        return dp(0,0,-1)


        