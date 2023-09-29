class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        return self.searchHelper(matrix, target)

    def searchHelper(self, matrix, target):
        # print(matrix)
        if len(matrix) < 1:
            return False
        elif len(matrix) == 1:
            return self.searchRow(matrix[0], target)

        mid = len(matrix)//2
        endVal = matrix[mid][-1]
        startVal = matrix[mid][0]
        if target > endVal:
            return self.searchHelper(matrix[mid+1:], target)
        elif target < endVal:
            if target > startVal:
                return self.searchRow(matrix[mid], target)
            elif target < startVal:
                return self.searchHelper(matrix[:mid], target)
        return True

    def searchRow(self, row, target):
        # print(row)
        if len(row) < 1:
            return False
        mid = len(row)// 2
        midVal = row[mid]
        # print(target, midVal)
        if target > midVal:
            return self.searchRow(row[mid+1:], target)
        elif target < midVal:
            return self.searchRow(row[:mid], target)
        return True
        

nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
val = 3

nums = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
val = 2

nums = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
val = 10

a = Solution().searchMatrix(nums, val)
print(a)  