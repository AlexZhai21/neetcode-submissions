class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Formula for
        ans = 0
        l = 0
        r = len(heights) - 1
    
        #r - l  equals distance between left and right (width of the container)
        while l < r:
            height = min(heights[l], heights[r])
            width = r - l 
            area = height * width
            if area > ans:
                ans = area
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: #if the next value of the right and left are equal or one sides next value is larger than the other sides next value but the next value is smaller than the current value
                if heights[l + 1] < heights[r - 1]:
                    r -= 1
                else:
                    l += 1

        return ans

        