class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            buy_price = prices[buy]
            sell_price = prices[sell]
            profit = sell_price - buy_price
            if profit > ans:
                ans = profit
            if sell_price < buy_price:
                buy = sell
                sell += 1
            else:
                sell += 1
        return ans

          







        