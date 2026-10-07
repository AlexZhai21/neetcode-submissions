class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #obstacle is 1, cant go to 1
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        tracker = {}
        
        def dp(x, y):
            if x >= rows or y >= cols:
                return 0
            if obstacleGrid[x][y] == 1:
                return 0
            
            if (x, y) in tracker:
                return tracker[(x, y)]
            if x == rows -1 and y == cols - 1:
                return 1

            ans = dp(x + 1, y) + dp(x, y + 1)
            tracker[(x, y)] = ans
            return ans
        return dp(0,0)
        