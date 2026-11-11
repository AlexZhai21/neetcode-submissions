from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        fresh_fruits = 0
        ans = 0
        rots = deque([]) #queue
        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    fresh_fruits += 1
                elif grid[x][y] == 2:
                    rots.append([x, y, 0]) #x, y, "level" aka time elapsed
        #multisource bfs
        dirs = [(1, 0), (-1, 0), (0,1), (0,-1)]
        while rots:
            x, y, time = rots.popleft()
            #x coordintae of the rotton fruit, y coordinate of the orttonf ruit, time in which it wasr otted
            for d in dirs:
                x_next = x + d[0]
                y_next = y + d[1]
                if x_next >= 0 and x_next < rows and y_next >= 0 and y_next < cols and grid[x_next][y_next] == 1: #if its a fresh fruit
                    grid[x_next][y_next] = 2
                    fresh_fruits -= 1
                    rots.append([x_next, y_next, time + 1])
            ans = time

        if fresh_fruits > 0:
            return -1
        return ans
        
        
        

        