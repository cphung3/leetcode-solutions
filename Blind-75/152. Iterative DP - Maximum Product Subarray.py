# Given an integer array nums, find a contiguous non-empty subarray within the
# array that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

# A subarray is a contiguous subsequence of the array.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        maxP, minP = 1, 1

        for n in nums:
            if n == 0:
                maxP, minP = 1, 1
                continue
            tmp = n * maxP
            maxP = max(n * maxP, n * minP, n)
            minP = min(tmp, n * minP, n)

            res = max(res, maxP)

        return res

# Runtime: 107 ms, faster than 75.46% of Python3 online submissions for Maximum Product Subarray.
# Memory Usage: 14.4 MB, less than 79.11% of Python3 online submissions for Maximum Product Subarray.