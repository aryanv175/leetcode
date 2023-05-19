# 62. Unique Paths
"""Logic: Second Problem: 62. Unique Paths
          Here we will make a matrix that contains the number 
          of ways we can reach any spot in the matrix. For e.g. 
          # is the initial spot of the robot.
          0   1   2   3   4
          0 #   1   1   1    1
          1  1   2   3   4   5
          2  1   3   6  10 15
          The last element of this matrix will give us the number 
          of ways we can reach that spot."""

def uniquePaths(m, n):
    # starting with a matrix with 0 for every spot.
    path = [[0]*m]*n

    # ways to reach any block in the starting row or column is 1.
    for i in range(m):
        path[0][i] = 1

    for i in range(n):
        path[i][0] = 1

    # now for every cell in the matrix we have the number of ways we can reach it.
    for row in range(1, n):
        for col in range(1, m):

            path[row][col] = path[row-1][col] + path[row][col-1]

    return path[-1][-1]
