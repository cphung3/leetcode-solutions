

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True

        max_idx = 0

        for i in range(len(nums)):
            if max_idx <= i and nums[i] == 0:
                return False

            if i + nums[i] > max_idx:
                max_idx = i + nums[i]

            if max_idx >= len(nums)-1:
                return True
        return False
