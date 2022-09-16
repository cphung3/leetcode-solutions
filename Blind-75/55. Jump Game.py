class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(goal-1, -1, -1):
            if nums[i] >= goal - i:
                goal = i

        return True if goal == 0 else False

# Runtime: 984 ms, faster than 30.33% of Python3 online submissions for Jump Game.
# Memory Usage: 15.3 MB, less than 18.22% of Python3 online submissions for Jump Game.