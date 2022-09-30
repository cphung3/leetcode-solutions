# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
# Example 2:

# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.

# class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     dp = [0] * len(nums)
    #     for i in range(len(nums)-1, -1, -1):
    #         for j in range(i + 1, len(nums)):
    # def rob(self, nums: List[int]) -> int:
    #     dp = [None] * len(nums)

    #     def recurse(nums, i):
    #         if dp[i]:
    #             return dp[i]

    #         value = nums[i]
    #         robHouse = recurse(nums, i - 1)
    #         dontRobHouse = value + recurse(nums, i - 2)
    #         profit = max(robHouse, dontRobHouse)
    #         dp[i] = profit

    #         return profit
            
    #     recurse(nums, len(nums)-1)
    #     return dp[len(nums)-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        r1, r2 = 0,0
        for n in nums:
            temp = max(n + r1, r2)
            r1 = r2
            r2 = temp
        return r2

# Runtime: 31 ms, faster than 95.48% of Python3 online submissions for House Robber.
# Memory Usage: 13.8 MB, less than 97.49% of Python3 online submissions for House Robber.