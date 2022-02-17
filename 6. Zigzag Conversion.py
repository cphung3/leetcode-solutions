class Solution:
    def convert(self, s: str, numRows: int) -> str:
        output = []
        if numRows == 1: return s
        if len(s) < numRows: return s
        iterations = len(s) // numRows + 1

        baseIdx = 2 * (numRows - 1)

        for curRow in range(numRows):
            for iter in range(iterations):
                # add the col elements
                colIdx = (iter * baseIdx) + curRow
                # print('info: ', baseIdx, colIdx, len(output))
                if colIdx > len(s) - 1: continue
                output.append(s[colIdx])
                
                
                # print()
                # add the diagonal elements if they exist
                if curRow != 0 and curRow != numRows - 1:
                    diagIdx = ((iter+1) * baseIdx) - (2 * curRow) + curRow
                    # print('diag: ----',  curRow, diagIdx)
                    if diagIdx > len(s) - 1: continue
                    output.append(s[diagIdx])
                    
        # print()
        return ''.join(output)

# Runtime: 136 ms, faster than 16.28% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 13.9 MB, less than 93.16% of Python3 online submissions for Zigzag Conversion.

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        l = len(s)
        arr=["" for x in range(l)]
        row = 0
        for i in range(l):
            arr[row] += s[i]
            if row == numRows - 1:
                down = False

            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        # Print concatenation
        # of all rows
        final = ""
        for i in range(l):
            final += arr[i]
        return final

# Runtime: 64 ms, faster than 78.27% of Python3 online submissions for Zigzag Conversion.
# Memory Usage: 14.2 MB, less than 75.52% of Python3 online submissions for Zigzag Conversion.