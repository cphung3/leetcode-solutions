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