class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        diags = []
        #boundary is n x n

        def backtracker(path, placed):
    
            if len(path) > 0:
                for x in [len(path) - 1]:
                    y = path[x].find("Q")
                        #x, y is the position of the queen we validate
                    diagonals = []
                    x_dirs = [1, -1]
                    y_dirs = [1, -1]
                        
                    for x_d in x_dirs:
                        for y_d in y_dirs:
                            curr_x = x
                            curr_y = y 
                            while curr_x + x_d < len(path) and curr_x + x_d >= 0 and curr_y + y_d < n and curr_y + y_d >= 0:
                                diagonals.append([curr_x + x_d, curr_y + y_d])
                                curr_x += x_d
                                curr_y += y_d
                    
                    for i in diagonals:
                        x_pos = i[0]
                        y_pos = i[1]
                        if path[x_pos][y_pos] == "Q":
                            return
                    #check if valid
                    if len(path) == n:
                        ans.append(path[:])
            for i in range(n):
                if i not in placed:
                    new_row = ["."] * n
                    new_row[i] = "Q"
                    new_row = "".join(new_row)
                    path.append(new_row)
                    placed.append(i)
                    backtracker(path, placed)
                    path.pop()
                    placed.pop()
            
        backtracker([], placed = [])
     
        return ans


#for point 2,2:
#diagonals are 0,0, 1,1, 3,3, 1,3, 3,1
# (+1, + 1), (+ 1, - 1), (- 1, + 1), (-1, -1)
        