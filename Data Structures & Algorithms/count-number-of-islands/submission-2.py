from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        #
         #o(nxm) time, we at most visit each thing once
        #space would be o(nxm), seen and starts can at most hold up to nxm things
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(1, 0), (-1, 0), (0,1), (0,-1)]
        def bfs(x, y):
            grid[x][y] = "0"
            q = deque([(x, y)])
            while q:
                top = q.popleft()
                for d in dirs:
                    x_next = top[0] + d[0]
                    y_next = top[1] + d[1]
                    if x_next >= 0 and x_next < rows and y_next >= 0 and y_next < cols and grid[x_next][y_next] == "1":
                        grid[x_next][y_next] = "0"
                        q.append((x_next, y_next))

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == "1":
                    bfs(x, y)
                    ans += 1
        return ans

            

   
            

        