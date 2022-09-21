class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        largestEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= largestEnd:
                largestEnd = end
            else:
                res += 1
                largestEnd = min(end, largestEnd)
        return res

# Runtime: 3342 ms, faster than 10.98% of Python3 online submissions for Non-overlapping Intervals.
# Memory Usage: 52.7 MB, less than 60.76% of Python3 online submissions for Non-overlapping Intervals.