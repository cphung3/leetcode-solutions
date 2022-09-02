class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n-1)
            res += 1
        return res

# Runtime: 42 ms, faster than 71.39% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.8 MB, less than 50.43% of Python3 online submissions for Number of 1 Bits.