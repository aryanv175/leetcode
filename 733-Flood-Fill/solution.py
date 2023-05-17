# 733. Flood Fill
""" Logic: This question was quite straight forward. We 
           recursively find the find the points which are 
           connected to the starting pixel and are of the 
           same color."""

def floodFill(image, sr, sc, newColor):
    startColor = image[sr][sc]
    seen = set()

    def dfs(i: int, j: int) -> None:
        if i < 0 or i == len(image) or j < 0 or j == len(image[0]):
            return
        if image[i][j] != startColor or (i, j) in seen:
            return

        image[i][j] = newColor
        seen.add((i, j))

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    dfs(sr, sc)
    return image
