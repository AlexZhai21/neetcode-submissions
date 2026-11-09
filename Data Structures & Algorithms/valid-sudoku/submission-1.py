class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rt = {} #will contain 9 things 0: set of things in there
        ct = {} #wilkl contain 9 things
        bt = {}
        for i in range(9):
            rt[i] = set()
            ct[i] = set()
        corners = [0, 3, 6]
        for i in corners:
            for j in corners:
                bt[(i, j)] = set()
        rows = len(board)
        cols = len(board[0])
        for x in range(rows):
            for y in range(cols):
                curr = board[x][y]
                if curr != '.' and curr in rt[x]:
                    return False
                if curr != '.' and curr in ct[y]:
                    return False
                rt[x].add(curr)
                ct[y].add(curr)
                x_cor = x//3 * 3
                y_cor = y//3 * 3
                if curr in bt[(x_cor, y_cor)] and curr != '.':
                    return False
                bt[(x_cor, y_cor)].add(curr)
        return True
        
        #(0,0), #(0,3) (0,6)
        #(3, 0) (3, 3), (3, 6)


       
        