class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        vals = [1] * len(nums) 

        prefix = 1
        for i, n in enumerate(nums):
            vals[i] = prefix
            prefix *= n
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            vals[j] *= postfix
            postfix *= nums[j]
        
        return vals

# Runtime: 289 ms, faster than 75.13% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 21.3 MB, less than 49.53% of Python3 online submissions for Product of Array Except Self.