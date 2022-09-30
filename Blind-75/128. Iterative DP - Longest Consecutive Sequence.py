# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        neighbors = set(nums)
        sequences = []

        longest = 0

        for n in nums:
            # check if it is start of sequence
            if n-1 not in neighbors:
                startSeq = n + 1
                longest += 1
                while startSeq in neighbors:
                    longest += 1
                    startSeq += 1
                sequences.append(longest)
                longest = 0
        return max(sequences)

    def longestConsecutive(self, nums: List[int]) -> int:
        neighbors = set(nums)
        longest = 0

        for n in nums:
            # check if it is start of sequence
            if n-1 not in neighbors:
                length = 0
                while n + length in neighbors:
                    length += 1
                longest = max(length, longest)
        return longest

# Runtime: 3565 ms, faster than 14.35% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 28.9 MB, less than 49.96% of Python3 online submissions for Longest Consecutive Sequence.

# Runtime: 2637 ms, faster than 27.92% of Python3 online submissions for Longest Consecutive Sequence.
# Memory Usage: 28.9 MB, less than 39.00% of Python3 online submissions for Longest Consecutive Sequence.