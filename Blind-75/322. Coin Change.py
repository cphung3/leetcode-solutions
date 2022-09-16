class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        coinSet = set(coins)

        for i in range(1, amount+1):
            coinRange = []
            for c in coins:
                if i in coinSet:
                    dp[i] = 1
                    break
                diff = i - c
                if diff < 0:
                    continue
                if diff in dp:
                    coinRange.append(1+dp[diff])
            if coinRange:
                dp[i] = min(coinRange)
        if amount in dp: return dp[amount]
        return -1

# Runtime: 3119 ms, faster than 24.55% of Python3 online submissions for Coin Change.
# Memory Usage: 14.8 MB, less than 34.15% of Python3 online submissions for Coin Change.