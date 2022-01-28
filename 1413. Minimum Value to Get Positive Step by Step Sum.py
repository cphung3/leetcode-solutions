class Solution:
    def minStartValue(self, nums):
        startValue = 1
        total = startValue
        for val in nums:
            total += val
            while total < 1:
                startValue += 1
                total += 1
        return startValue

nums = [1,-2,-3]
ans = Solution().minStartValue(nums)
print(ans)

# Runtime: 24 ms, faster than 97.36% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.
# Memory Usage: 14 MB, less than 98.68% of Python3 online submissions for Minimum Value to Get Positive Step by Step Sum.