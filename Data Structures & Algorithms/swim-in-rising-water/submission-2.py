class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_t = float('-inf')
        min_t = float('inf')
        for i in range(n):
            for j in range(n):
                if grid[i][j] > max_t:
                    max_t = grid[i][j]
                if grid[i][j] < min_t:
                    min_t = grid[i][j]
        l = min_t
        r = max_t
        print(min_t)
        print(max_t)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        def dfs(i, j, t):
            if grid[i][j] > t:
                return False
            if i == n-1 and j == n-1:
                return True
            if (i, j) in seen:
                return False
            
            seen.add((i, j))
            for d in dirs:
                i_new = i + d[0]
                j_new = j + d[1]
                if i_new >= 0 and j_new >= 0 and j_new < n and i_new < n:
                    if dfs(i_new, j_new, t):
                        return True
            
            return False
        seen = set()
        ans = float('inf')
        while l <= r:
            m = l + (r-l)//2
            print(m)
            if dfs(0, 0, m):
                ans = m
                r = m - 1
            else:
                l = m + 1
            seen = set()
        return ans


