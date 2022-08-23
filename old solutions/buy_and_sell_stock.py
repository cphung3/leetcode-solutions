
    def maxProfit(self, prices: List[int]) -> int:
        min_val = max(prices)
        max_val = 0

        for i in prices:
            if i < min_val:
                min_val = i
            elif i - min_val > max_val:
                max_val = i - min_val
        return max_val