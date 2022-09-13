class Solution:
    def climbStairs(self, n: int) -> int:
        s1, s2 = 1, 1
        res = 0
        if n == 1:
            return 1
        for i in range(n-1):
            res = s1 + s2
            s2 = s1
            s1 = res
        return res