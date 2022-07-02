import math
class Solution:
    def numSquares(self, n: int) -> int:
        all_exprs = []
        # get the sq root of the number
        sqrt = math.floor(n**(1/2))

        # subtract from the result 
        diff = n - sqrt
        expr = []
        expr.append(sqrt)

        while diff != 0:



        