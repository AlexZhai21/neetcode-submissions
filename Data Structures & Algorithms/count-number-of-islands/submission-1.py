class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        #
        starts = []
        rows = len(grid)
        cols = len(grid[0])
        seen = set()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    starts.append([x, y])
        dirs = [(1, 0), (-1, 0), (0,1), (0,-1)]
        def dfs(x, y):
            if (x, y) in seen:
                return
            seen.add((x, y))
            for d in dirs:
                x_next = x + d[0]
                y_next = y + d[1]
                if x_next >= 0 and x_next < rows and y_next >= 0 and y_next < cols and grid[x_next][y_next] == "1":
                    dfs(x_next, y_next)
            return 1

        for s in starts:
            x = s[0]
            y = s[1]
            if (x, y) in seen:
                continue
            else:
                ans += dfs(x, y)
        return ans
            

        