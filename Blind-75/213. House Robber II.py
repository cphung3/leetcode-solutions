class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        r1, r2 = 0,0
        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp
        return r2

# Runtime: 42 ms, faster than 73.81% of Python3 online submissions for House Robber II.
# Memory Usage: 13.8 MB, less than 98.20% of Python3 online submissions for House Robber II.