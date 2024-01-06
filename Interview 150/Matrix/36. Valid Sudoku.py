class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        listSquares = [(1,1), (1,4), (1,7), (4,1), (4,4), (4,7), (7,1), (7,4), (7,7)]
        squares = set(listSquares)

        # check each row, col, and square from range 0-9
        for i in range(9):
            col = set()
            row = set()
            for j in range(9):
                rowVal = board[i][j]
                if (i, j) in squares:
                    ans = self.checkSquare(i,j,board)
                    if not ans:
                        return False
                if rowVal == '.': pass
                elif rowVal in row:
                    # print('row', rowVal, row)
                    return False
                else:
                    row.add(rowVal)

                colVal = board[j][i]
                # print(colVal, i, j, col)
                if colVal == '.': pass
                elif colVal in col:
                    # print('col', colVal, col)
                    return False
                else:
                    col.add(colVal)
        return True
        
    def checkSquare(self, i, j, board):
        top = [(i - 1, j-1), (i, j - 1), (i + 1, j -1)]
        mid = [(i - 1, j), (i, j), (i + 1, j)]
        bot = [(i - 1, j+1), (i, j+1), (i + 1, j+1)]
        neighbors = top + mid + bot
        squ = set()

        # print()
        # print('initial', i, j)
        for x,y in neighbors:
            sqVal = board[x][y]
            # print(sqVal, x,y)
            if sqVal == '.': pass
            elif sqVal in squ:
                # print(sqVal, squ)
                return False
            else:
                squ.add(sqVal)
        return True

a = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

b = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

c = [[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

d = [["7",".",".",".","4",".",".",".","."],[".",".",".","8","6","5",".",".","."],[".","1",".","2",".",".",".",".","."],[".",".",".",".",".","9",".",".","."],[".",".",".",".","5",".","5",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".","2",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]

tests = [a,b,c,d]

for i in tests:
    a = Solution().isValidSudoku(i)
    print(a)  
    print()