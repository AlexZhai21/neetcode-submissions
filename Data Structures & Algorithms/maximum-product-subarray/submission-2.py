class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tracker = {}
        n = len(nums)
        #when you get zero, you wanna remove that form your array because u are then limited by zro
        #idea: track how many negatives are in your current product
        neg = 0
        ans = float('-inf')
        for i in nums:
            if i < 0:
                neg += 1
        #neg tells us how much negaive nubmers we have remaining, 
        #if you have a positive number, than even amoutn of negative numbers is good, if odd then you gota srhink once you get tot he odd one
        #if you have a negtative nubmer, than odd amoutn of negatie nubmers is good, once you get to an even amount you shoudl start shrinking
        #once you see a zero, you increment the window to be past that but store 0 as a potential answer, then keep going
    
        #if you hvae no zeros in your subarray and you have an even number of negatives, then shrinking your array is for sure going to make it smaller
        l, r = 0,0
        curr_p = [1, False]
        while r < n:
            curr = nums[r]
            if curr == 0:
                ans = max(0, ans)
                curr_p = [1, False]
                l = r + 1 #if see 0, skip it immediatly, it limits your rpoduct
            else:
                curr_p[0] *= curr
                curr_p[1] = True
                ans = max(curr_p[0], ans)
                if curr < 0:
                    neg -= 1 #you have one less engative aavialbe in your array
                    #if you are negative and there are no negatives left, gotta increment left pointer until you are positive
                    while curr_p[0] < 0 and neg == 0: #if you are negative and thers no more engatives to offset you, keep oging until you are positive again
                        curr_p[0] //= nums[l]
                        l += 1
                        if l >= r:
                            curr_p[1] = False
                if curr_p[1]:
                    ans = max(curr_p[0], ans)
            r += 1
        return ans
