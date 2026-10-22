from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        col = len(board[0])
        start = word[0]
        starts = []
        dirs = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        for x in range(rows):
            for y in range(col):
                if board[x][y] == start:
                    starts.append([x, y])
        #multisource dfs
        print(starts)
        seen = set()
        def backtrack(x, y, left):
            if (x, y) in seen:
                return False
            
            if board[x][y] != left[0]:
                return False
            seen.add((x, y))
            to_remove = left.popleft()
    
            if not left:
                return True
            for d in dirs:
                x_next = x + d[0]
                y_next = y + d[1]
                if x_next >= 0 and x_next < rows and y_next >= 0 and y_next < col:
                    if backtrack(x_next, y_next, left) == True:
                        return True

            seen.remove((x, y))
            left.appendleft(to_remove)
        der_deque = deque(word)
        for i in starts:
            if backtrack(i[0], i[1], der_deque) == True:
                return True
        return False


        