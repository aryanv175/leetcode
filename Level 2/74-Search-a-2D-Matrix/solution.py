class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # we find the row which contains the value that we need by using the last value in that row
        # if the last value  of a row is bigger than the target value then, target is in that row
        row = i =  0 
        while i in range(len(matrix)): # use  a while loop until the break statement occurs
            if target > matrix[i][-1] and row + 1 < len(matrix): # explained above
                row += 1
            else:
                break
            i+= 1
        
        return target in matrix[row] # return if the target is in the row we got from the loop!
