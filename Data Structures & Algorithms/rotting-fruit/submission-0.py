from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = set()
        tracker = deque()
        rows = len(grid)
        cols = len(grid[0])
        num_total_fruits = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    tracker.append((x, y, 0)) #coordinate + minutes
                    num_total_fruits += 1
                if grid[x][y] == 1:
                    num_total_fruits += 1
        ans = 0
        while tracker:
            curr_fruit = tracker.popleft()
            x = curr_fruit[0]
            y = curr_fruit[1]
            curr_mins = curr_fruit[2]
            if (x, y) in visited:
                continue
            visited.add((x, y))
            ans = max(ans, curr_mins)
            for d in dirs:
                x_n = x + d[0]
                y_n = y + d[1]
                if x_n >= 0 and x_n < rows and y_n >= 0 and y_n < cols and grid[x_n][y_n] != 0:
                    tracker.append((x_n, y_n, curr_mins + 1))
        if len(visited) == num_total_fruits:
            return ans
        return -1




        #do a check if number of coordinates visited = num_total_fruits
