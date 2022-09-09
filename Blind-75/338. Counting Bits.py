class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        
        return dp

# Runtime: 229 ms, faster than 22.34% of Python3 online submissions for Counting Bits.
# Memory Usage: 20.7 MB, less than 79.16% of Python3 online submissions for Counting Bits.