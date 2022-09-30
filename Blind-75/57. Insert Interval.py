class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        # Completely encompasses an interval: 
        # newI[0] < i[0], newI[1] > i[1] -> Remove entire interval of i

        # Partial encompass
        # newI[0] > i[0], newI[1] > i[1] -> Replace i[1] with newI[1]
        # newI[0] < i[0], newI[1] < i[1] -> Replace i[0] with newI[0]
        res = []
        startOverlap = False
        temp = []
        s, e = newInterval[0], newInterval[1]
        for inter in intervals:
            s_i, e_i = inter[0], inter[1]

            if s >= s_i or s <= e_i:
                startOverlap = True
                temp.append(s_i)
            elif s < s_i:
                # skip this interval
                pass
            elif s > e_i or s_i > e:
                # add this interval, but no overlap
                res.append(inter)
            
            if startOverlap:
                # check if end is overlapping
                if e <= e_i and e >= s_i:
                    newEnd = e_i
                elif s_i > e:
                    newEnd = e
                if newEnd:
                    temp.append(newEnd)
            
            if len(temp) == 2:
                res.append(temp)
                startOverlap = False

        return res

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Ending of new interval is smaller than start of current one
            # so just insert at beginning
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # Start of new interval is bigger than end of current one
                # so just append the current interval and wait
                res.append(intervals[i])
            else:
                # There is overlap so the new start will be the earlier start
                # and the new end will be the later end
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        
        res.append(newInterval)
        return res

# Runtime: 82 ms, faster than 95.79% of Python3 online submissions for Insert Interval.
# Memory Usage: 17.3 MB, less than 91.85% of Python3 online submissions for Insert Interval.