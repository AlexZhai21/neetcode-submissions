class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        tracker = {}
        def dp(i, total):
            if (i, total) in tracker:
                return tracker[(i, total)]
            if total < 0:
                return 0
            #at each timestep, you can either use this coin, not use this coin and mvoe on
            if total == 0:
                return 1
            if i >= n:
                return 0
            curr_coin = coins[i]
            ans = dp(i, total - curr_coin) + dp(i + 1, total)
            tracker[(i, total)] = ans

            return ans
        return dp(0,amount)


        #dp i + 1, total - curr_coin is repeeitive, it will be dealt with after so tis overcounting



