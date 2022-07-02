class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        
        while l < r and r < len(prices):
            if prices[l] < prices[r]:
                diff = prices[r] - prices[l]
                maxProfit = max(maxProfit, diff)
            else:
                l = r
            r += 1
        return maxProfit

# Runtime: 1169 ms, faster than 82.18% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Memory Usage: 25 MB, less than 37.94% of Python3 online submissions for Best Time to Buy and Sell Stock.