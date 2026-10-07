# class Solution:
#     def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
#         ans = []
#         pacific = set()
#         atlantic = set()
#         rows = len(heights)
#         cols = len(heights[0])
#         seen = set()
#         dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
#         def searcher(x, y):
#             if (x,y) in seen:
#                 return
#             seen.add((x, y))
#             for d in dirs:
#                 if x + d[0] >= 0 and x + d[0] < rows and y + d[1] >= 0 and y + d[1] < cols and heights[x][y] >= heights[x + d[0]][y + d[1]]:
#                     searcher(x + d[0], y + d[1])
#                 if (x + d[0], y + d[1]) in pacific and heights[x + d[0]][y + d[1]] <= heights[x][y]: #borders the pacific  or can access smth with access to teh pacific ocdan
#                     pacific.add((x, y))
#                 if (x + d[0], y + d[1]) in atlantic and heights[x + d[0]][y + d[1]] <= heights[x][y]: #borders the atlatnci ocean or can access smth in atlantic
#                     atlantic.add((x, y))
                
                
#         for i in range(cols):
#             pacific.add((0, i))
#         for i in range(cols):
#             atlantic.add((rows -1, i))
#         for i in range(rows):
#             pacific.add((i, 0))
#             atlantic.add((i, cols - 1))
#         for r in range(rows):
#             for c in range(cols):
#                 searcher(r, c)

#         interset = pacific.intersection(atlantic)
#         for i in interset:
#             ans.append(list(i))
#         return ans

                




#         #first row and first column automatically get the pacific
#         #row index -1 is pacific, col index of -1 is also pacific

#         #last row and last column automatically get the atlatnc
#         #row index + 1s in atlatnci, col_index + 1 is atlantic
#         #any thing in both automatically is part of the answer
        
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ans = []
        pacific = set()
        atlantic = set()

        rows = len(heights)
        cols = len(heights[0])

        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def searcher(x, y, ocean):
            if (x, y) in ocean:
                return

            ocean.add((x, y))

            for d in dirs:
                new_x = x + d[0]
                new_y = y + d[1]

                if (
                    new_x >= 0
                    and new_x < rows
                    and new_y >= 0
                    and new_y < cols
                    and heights[new_x][new_y] >= heights[x][y]
                ):
                    searcher(new_x, new_y, ocean)

        # start DFS from Pacific borders
        for i in range(cols):
            searcher(0, i, pacific)

        for i in range(rows):
            searcher(i, 0, pacific)

        # start DFS from Atlantic borders
        for i in range(cols):
            searcher(rows - 1, i, atlantic)

        for i in range(rows):
            searcher(i, cols - 1, atlantic)

        interset = pacific.intersection(atlantic)

        for i in interset:
            ans.append(list(i))

        return ans