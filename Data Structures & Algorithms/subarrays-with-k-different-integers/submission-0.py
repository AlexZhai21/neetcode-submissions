class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        window = {}
        ll = 0
        lr = 0
        r = 0
        ans = 0
        while r < len(nums):
            window[nums[r]] = r
            while len(window) > k:
                if window[nums[ll]] == ll: #lr is the right most left boundary
            
                    window.pop(nums[ll])
                ll += 1
            if lr < ll:
                lr = ll
            while len(window) == k:
            
                if window[nums[lr]] == lr:
                    ans += lr - ll + 1
                    break
                else:
                    lr += 1
           
            r += 1
        

        return ans

        