class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        # idea behind solving this problem:
        # run the loop, num_of_balls = no of columns times.
        # cases to consider:
        # first we will see the cases the ball is stuck
        # 1. if the board directs the ball to the left and it is at column 0, then the ball gets stuck. (1)
        # similarily if the board directs the ball to the right and the ball is at the last column, the ball gets stuck. (2)
        # 2. if the current cell grid[i][j] = 1 and grid[i][j+ 1] == -1, we have a V shape and the ball gets stuck. (3)
        # similarily if the current cell grid[i][j] = -1 and grid[i][j-1] == 1. we have a V shape and the ball gets stuck. (4)
        # now the case where the ball does not get stuck
        # if the current cell grid[i][j] = 1 then next one will be grid[i+1][j+1] (5)
        # and if the current cell grid[i][j] = -1 then next one will be grid[i+1][j-1] (6)
        # note that i will increase by one every time regardless of the direction if the ball is not stuck, as it is falling down.
        # thats it!

        def wbf(grid, i): # wbf = where ball fall lol
            col = i 
            for row in range(len(grid)):
                if grid[row][col] == 1: # board directing right
                    if col +1 == len(grid[0]):  # (3) stuck by wall
                        return - 1
                    elif grid[row][col+1] == -1:  # (4) V shape
                        return -1
                    col+= 1 # (5)
                else: # board directing left
                    if col == 0: # (1) stuck by wall
                        return - 1
                    elif grid[row][col-1] == 1: # (2) V shape
                        return -1     
                    col-= 1  # (6)                      
            return col
           
        num_balls = len(grid[0]) # columns
        answer = [] # array to store the answers
        for i in range(num_balls): # loop runs as many times as the number of balls
            answer.append(wbf(grid, i)) 
        return answer # return!
