class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        num_rows = len(image)
        num_cols = len(image[0])
        orig_color = image[sr][sc]
        def filler(x, y):
            if image[x][y] != color and image[x][y] == orig_color:
                image[x][y] = color
                for dirs in [(1, 0), (0, 1), (-1, 0), (0, -1)]: #all the nearby neighbors
                    if x + dirs[0] >= 0 and x + dirs[0] < num_rows and y + dirs[1] >= 0 and y + dirs[1] < num_cols:
                        filler(x +dirs[0], y +dirs[1])
        
        filler(sr, sc)
        return image





        #start from sr, sc
        #neighbors include sr +- 1, sc +- 1

        