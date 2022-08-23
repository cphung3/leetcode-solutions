


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Consider all squares one by one 
        N = len(matrix)
        for x in range(0, int(N/2)): 
              
            # Consider elements in group    
            # of 4 in current square 
            for y in range(x, N-x-1): 
                  
                # store current cell (bottom) in temp variable 
                temp = matrix[N-1-x][N-1-y]
      
                # move values from right to bottom 
                # then top to right
                # then left to top 
                # then bottom to left
                # matrix[x][y] = matrix[y][N-1-x] 
                matrix[N-1-x][N-1-y] = matrix[y][N-1-x] 

                matrix[y][N-1-x] = matrix[x][y]

                matrix[x][y] = matrix[N-1-y][x]

                matrix[N-1-y][x] = temp
                

# Python3 program to rotate a matrix by 90 degrees 
N = 4
  
# An Inplace function to rotate  
# N x N matrix by 90 degrees in 
# anti-clockwise direction 
def rotateMatrix(mat): 
      
