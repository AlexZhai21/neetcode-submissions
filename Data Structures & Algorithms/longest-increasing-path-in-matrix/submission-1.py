class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        tracker = {}
        rows = len(matrix)
        cols = len(matrix[0])
        dirs = [(1,0), (0,1), (-1, 0), (0,-1)]
        ans = []
        def dp(x, y):
        
            der_val = matrix[x][y]
            if (x, y) in tracker:
                return tracker[(x, y)]
            ans = [1]
            for d in dirs:
                x_next = x+d[0]
                y_next = y + d[1]
                if x_next >= 0 and x_next < rows and y_next >= 0 and y_next < cols:
                    if der_val < matrix[x_next][y_next]:
                        
                        ans.append(1 + dp(x_next, y_next))
            tracker[(x, y)] = max(ans)
            return max(ans)
        for x in range(rows):
            for y in range(cols):
                ans.append(dp(x, y))
        return max(ans)


           