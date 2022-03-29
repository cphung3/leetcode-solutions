class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        l, r = 0, length - 1
        jumps = 0
        while r > 0 and l < length:
            if (r - l) - nums[l] <= 0:
                r, l = l, 0
                jumps += 1
                continue
            l += 1
        return jumps

# Runtime: 1988 ms, faster than 32.20% of Python3 online submissions for Jump Game II.
# Memory Usage: 15.2 MB, less than 42.45% of Python3 online submissions for Jump Game II.