class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #longest subsquence of two distinct elements
        tracker = {} #fruit: most recent index
        l = 0
        r = 0
        ans = 0
        curr_frts = 0
        n = len(fruits)
        while r < n:
            der_fruit = fruits[r]
            tracker[der_fruit] = r #most recent time you seen this, so we know whats the last occurance of this fruit type inour basket
            curr_frts += 1
            while len(tracker) > 2:
                if tracker[fruits[l]] == l:
                    tracker.pop(fruits[l])
                l += 1
                curr_frts -= 1
            ans = max(ans, curr_frts)
            r += 1
        
        return ans
            


        