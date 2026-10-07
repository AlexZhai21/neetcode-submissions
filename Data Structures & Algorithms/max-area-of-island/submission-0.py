class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        seen = set() #set of x, ys to know where weve already searched
        num_rows = len(grid)
        num_cols = len(grid[0])
        def dfs(x, y):
            if (x,y) in seen:
                return 0
            else:
                seen.add((x, y))
            if grid[x][y] == 0:
                return 0
            else: #this is an unvisited island part
                dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
                other_islands = 0
                for d in dirs:
                    if x + d[0] >= 0 and x + d[0] < num_rows and y + d[1] >= 0 and y + d[1] < num_cols:
                        other_islands += dfs(x + d[0], y + d[1])

                return 1 + other_islands
        for x in range(num_rows):
            for y in range(num_cols):
                ans = max(ans, dfs(x, y))
        return ans


            
            
        