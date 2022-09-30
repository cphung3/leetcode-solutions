class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        seq = 0
        
        for i in range(len(nums)):
            if seq < 0:
                seq = 0
            seq += nums[i]
            maxSoFar = max(seq, maxSoFar)
        return maxSoFar

# Runtime: 1043 ms, faster than 60.14% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 27.9 MB, less than 78.35% of Python3 online submissions for Maximum Subarray.