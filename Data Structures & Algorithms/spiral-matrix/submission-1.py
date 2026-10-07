class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #dirs
        #right, down, left, up
        dirs = [(0,1), (1, 0), (0, -1), (-1,0)]
        rows = len(matrix)
        cols = len(matrix[0])
        ans = []
        num_ans = 0
        needed_ans = rows * cols
        visited = set() #set of visited coordinates
        curr_dir = 0
        x = 0
        y = 0
        while num_ans < needed_ans:
            ans.append(matrix[x][y])
            num_ans += 1
            x_dir = dirs[curr_dir][0]
            y_dir = dirs[curr_dir][1]
            if x + x_dir < 0 or x + x_dir>= rows or y + y_dir < 0 or y + y_dir >= cols or (x + x_dir, y + y_dir) in visited:
                curr_dir = (curr_dir + 1) % 4
            visited.add((x, y))
            x += dirs[curr_dir][0]
            y += dirs[curr_dir][1]
        return ans

        