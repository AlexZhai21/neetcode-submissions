class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])
        der_rows = set()
        der_cols = set()
        for x in range(rows):
            for y in range(cols):
                if matrix[x][y] == 0:
                    der_rows.add(x)
                    der_cols.add(y)
        for x in range(rows):
            zeroed=False
            if x in der_rows:
                zeroed = True
            for y in range(cols):
                if zeroed:
                    matrix[x][y] = 0
                elif y in der_cols:
                    matrix[x][y] = 0
                

        
        