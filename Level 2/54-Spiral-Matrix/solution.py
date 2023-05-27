class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i = 0
        spiral = []
        up = 0
        left = 0
        right = len(matrix[0]) - 1
        down = len(matrix) - 1
        while up < down and left < right:
            # going left
            for i in range(left, right+1):
                spiral.append(matrix[up][i])


            up += 1  # top most row can no longer be touched

            # going down
            for i in range(up, down+1):
                spiral.append(matrix[i][right])


            right -= 1  # right most column can no longer be touched

            # going right
            for i in range(right, left-1, -1):
                spiral.append(matrix[down][i])


            down -= 1  # bottom row can no longer be touched

            # going up
            for i in range(down, up-1, -1):
                spiral.append(matrix[i][left])

            left += 1  # left most column can no longer be touched
        
        # edge cases
        if up == down == left == right:  # in case only one element is left or only one element is there
            for i in range(left, right + 1):
                spiral.append(matrix[up][i])
        elif up == down:  # column remaining, need to go left. or if there is only a column
            for i in range(left, right + 1):
                spiral.append(matrix[up][i])
        elif left == right:  # row remaining, need to go down, or if there is only a row
            for i in range(up, down + 1):
                spiral.append(matrix[i][right])

        return spiral
                    
