    
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Initialize:
#     max_so_far = 0
#     max_ending_here = 0

# Loop for each element of the array
#   (a) max_ending_here = max_ending_here + a[i]
#   (b) if(max_ending_here < 0)
#             max_ending_here = 0
#   (c) if(max_so_far < max_ending_here)
#             max_so_far = max_ending_here
# return max_so_far

    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        max_so_far = 0
        max_here = 0
        sub_length = 0

        for i in nums:
            max_here += i
            sub_length += 1
            if max_here < 0:
                max_here = 0
                sub_length = 0
            if max_so_far < max_here:
                max_so_far = max_here
        if sub_length == 0 and max_so_far == 0:
            return max(nums)
        return max_so_far