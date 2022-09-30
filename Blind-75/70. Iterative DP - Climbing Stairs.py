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

# Runtime: 55 ms, faster than 27.96% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14 MB, less than 11.85% of Python3 online submissions for Climbing Stairs.