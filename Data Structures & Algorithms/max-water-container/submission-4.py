class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        ans = 0
        while l <= r:
            width = r - l
            height = min(heights[l], heights[r])
            ans = max(width * height, ans)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return ans
        #my logic is that no matter what the next best bars are, it don matter becuse we are completley limited by the smalelst bar, so we should alays be tryna get rid of the slalest bar.


        