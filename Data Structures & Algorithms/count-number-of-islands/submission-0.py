class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        seen = set() #list of tuples of the places we already searched (either already part of an island or not yet)
        num_rows = len(grid)
        num_cols = len(grid[0])
        def island_tracker(x, y):
            if (x,y) in seen:
                return 0
            else:
                seen.add((x, y))
            if grid[x][y] == "0":
                return 0
            else: #not seen before and not 0, this a 1 that we havent seen (may be a new island may be part of another one if called recursively)
                dirs = [(1,0), (0,1), (-1, 0), (0, -1)]
                for d in dirs:
                    if x + d[0] >= 0 and x + d[0] < num_rows and y + d[1] >= 0 and y + d[1] < num_cols:
                        island_tracker(x + d[0], y + d[1])
                return 1
            
        for x in range(num_rows):
            for y in range(num_cols):
                #island tracker sth
                ans += island_tracker(x, y)
        return ans



        