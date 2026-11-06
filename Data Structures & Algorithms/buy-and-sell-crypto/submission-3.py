class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        #use r as a probe, doe it ever make sense to buy something at L if the price at L is more expensiev than R..? potentially, but only if the better price is in between L and R, which we will have already consiered by the time we reach R.
        #if it is mroe expensive at R than at our simulated starting price L, simualte a sell and continue
        #if R is cheaper than L, then we've already considered the potentail sells, so theres no reason to buy at L now since anything that better that occurs AFTER R, R is a better starting price ALWAYS
        l, r = 0,0
        days = len(prices)
        while r < days:
            curr_p = prices[r]
            sell_p = prices[l]
            if curr_p < sell_p:
                l = r
            else:
                ans = max(ans, curr_p - sell_p)
            r += 1
        return ans