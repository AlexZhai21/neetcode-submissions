from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        land = 2^31 - 1
        visited = set() #visited set for lands
        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])
        tracker = deque()
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    tracker.append((x, y, 0)) #coordinate, distance
     
        while tracker:
            top_node = tracker.popleft() #the thing in the top
            x = top_node[0]
            y = top_node[1]
            dist = top_node[2]
            if (x,y) in visited:
                continue
            else:
                visited.add((x, y))
            if grid[x][y] != 0 and grid[x][y] != -1:
                grid[x][y] = dist
            for d in dirs:
                x_n = x + d[0]
                y_n = y + d[1]
                if x_n >= 0 and x_n < rows and y_n >= 0 and y_n < cols and grid[x_n][y_n] != -1:
                    tracker.append((x_n, y_n, dist + 1))


        
       