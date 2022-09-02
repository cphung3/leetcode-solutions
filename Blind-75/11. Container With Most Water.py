class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        length = len(height) - 1
        maxArea = 0

        while l < r:
            maxHeight = min(height[l], height[r])
            maxArea = max(maxArea, length * maxHeight)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            length -= 1
        return maxArea

# Runtime: 1804 ms, faster than 5.02% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.5 MB, less than 12.88% of Python3 online submissions for Container With Most Water.