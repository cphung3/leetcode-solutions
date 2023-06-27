class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        highestCandies = max(candies)
        return [(i + extraCandies) >= highestCandies for i in candies]