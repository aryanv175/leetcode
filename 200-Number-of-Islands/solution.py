# 200. Number of Islands
""" Logic: Key Concept: Depth First Search
           To find the number of islands we move from 
           the top left to the bottom right. After every 
           move, if we find 0 or water we repeat the
           path until we find one island. After we find 
           an island, we update the count."""

def numIslands(grid):
    if not grid: return 0
    row = len(grid)
    col = len(grid[0])
    visited = set()
    count = 0
    directions=[(-1,0),(0,1),(1,0),(0,-1)]
    def findIsland(x,y):
        for dx, dy in directions:
            nx,ny = x+dx, y+dy
            if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1' \
            and (nx,ny) not in visited:
                visited.add((nx,ny))
                findIsland(nx,ny)
        
    for x in range(row):
        for y in range(col):
            if grid[x][y] == '1' and (x,y) not in visited:
                count +=1
                visited.add((x,y))
                findIsland(x,y)         
    return count
