class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = rows #is a square
        for x in range(rows): #row checker
            nums_seen = set()
            for y in range(cols):
                if board[x][y] != ".":
                    if board[x][y] in nums_seen:
                        return False
                    nums_seen.add(board[x][y])
            
        for y in range(cols):
            nums_seen = set()
            for x in range(rows):
                if board[x][y] != ".":
                    if board[x][y] in nums_seen:
                        return False
                    nums_seen.add(board[x][y])
        x_left = 0
        y_left = 0
        first = True
        while True:
            
            if x_left >= rows:
                x_left = 0
                y_left += 3
            if y_left >= cols:
                return True 
            coors_seen = []
            nums_seen = set()
            for x in range(3):
                x_val = x_left + x
                
                for y in range(3):
                    y_val = y_left + y
                    coors_seen.append((x_val, y_val))
                    if board[x_val][y_val] != ".":
                        if board[x_val][y_val] in nums_seen:
                            return False
                        nums_seen.add(board[x_val][y_val])
                first = False
            x_left += 3
        return True
