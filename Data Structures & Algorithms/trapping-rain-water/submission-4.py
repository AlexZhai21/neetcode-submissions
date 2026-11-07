class Solution:
    def trap(self, height: List[int]) -> int:
        #for each "left bar", the first right bar you see thats >= is the best one

        #[0,2,2,3,3,3,3,2,1]
        #left sweep
        left_wata = 0
        right_wata = 0
        curr_left = 0
        for l in range(len(height)):
            if height[curr_left] == 0:
                curr_left += 1
            elif height[l] >= height[curr_left] and curr_left != l:
                # print(f"to add from {curr_left} to {l} is {(height[curr_left] * (l - curr_left - 1))}")
        
                left_wata += (height[curr_left] * (l - curr_left - 1))
                p1 = curr_left + 1
                p2 = l -1
                while p1 <= p2:
                    left_wata -= height[p1]
                    p1 += 1
               

                curr_left = l
        curr_right = len(height) - 1
        for r in range(len(height) - 1, -1, -1):
            if height[curr_right] == 0:
                curr_right -= 1
            elif height[r] > height[curr_right]:
                right_wata += (height[curr_right] * (curr_right - r - 1))
                p1 = r + 1
                p2 = curr_right -1
                while p1 <= p2:
                    right_wata -= height[p1]
                    p1 += 1
                curr_right = r
        # print(left_wata)
        # print(right_wata)
        return left_wata + right_wata

            
        