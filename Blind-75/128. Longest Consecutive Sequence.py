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