class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1], [1,1]]
        if numRows == 2:
            return res
        for i in range(2, numRows):
            ans = [1]
            inner_list = res[-1]
            for j in range(1, len(inner_list)):
                ans.append(inner_list[j-1] + inner_list[j])
            ans.append(1)
            res.append(ans)
        return res
            

# Runtime: 37 ms, faster than 69.67% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 70.20% of Python3 online submissions for Pascal's Triangle.