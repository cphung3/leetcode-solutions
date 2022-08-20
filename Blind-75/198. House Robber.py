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