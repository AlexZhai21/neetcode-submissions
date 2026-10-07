class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = set()
        atlantic = set()
        rows = len(heights)
        cols = len(heights[0])
        p_seen = set()
        a_seen = set()
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        def searcher(x, y, seen):
            if (x,y) in seen:
                return
            seen.add((x, y))
            for d in dirs:
                if x + d[0] >= 0 and x + d[0] < rows and y + d[1] >= 0 and y + d[1] < cols and heights[x][y] <= heights[x + d[0]][y + d[1]]:
                    searcher(x + d[0], y + d[1], seen)
                # if (x + d[0], y + d[1]) in pacific and heights[x + d[0]][y + d[1]] <= heights[x][y]: #borders the pacific  or can access smth with access to teh pacific ocdan
                #     pacific.add((x, y))
                # if (x + d[0], y + d[1]) in atlantic and heights[x + d[0]][y + d[1]] <= heights[x][y]: #borders the atlatnci ocean or can access smth in atlantic
                #     atlantic.add((x, y))
                
                
        for i in range(cols):
            pacific.add((0, i))
            atlantic.add((rows -1, i))
        for i in range(rows):
            pacific.add((i, 0))
            atlantic.add((i, cols - 1))
        for t in pacific:
            searcher(t[0], t[1], p_seen)
        for t in atlantic:
            searcher(t[0], t[1], a_seen)
        pacific = pacific | p_seen
        atlantic = atlantic | a_seen
        interset = pacific.intersection(atlantic)
        for i in interset:
            ans.append(list(i))
        return ans

                




        #first row and first column automatically get the pacific
        #row index -1 is pacific, col index of -1 is also pacific

        #last row and last column automatically get the atlatnc
        #row index + 1s in atlatnci, col_index + 1 is atlantic
        #any thing in both automatically is part of the answer
        