class Solution:
    def solve(self, board: List[List[str]]) -> None:
        tracker = set() #set of (x,y) coordinates of "safe" O regions
        dirs = [(1, 0), (0, 1), (-1, 0), (0,-1)]
        rows = len(board)
        cols = len(board[0])
        def dfs(x, y):
            if board[x][y] == "X":
                return
            if (x, y) in tracker: #must be an O
                return
            tracker.add((x, y)) 
            for d in dirs:
                if x + d[0] >= 0 and x + d[0] < rows and y + d[1] >= 0 and y + d[1] < cols:
                    dfs(x + d[0], y + d[1])
        
        for x in range(rows):
            for y in range(cols):
                if (x == 0 or x == rows - 1 or y == 0 or y == cols - 1) and board[x][y] == "O":
                    dfs(x, y)
        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "O" and (x, y) not in tracker:
                    board[x][y] = "X"



        