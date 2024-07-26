"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        res = []

        idx = 0
        # Insert at the right position
        while idx < len(intervals):
            if idx == len(intervals) - 1:
                if intervals[idx][0] < newInterval[0]:
                    intervals.append(newInterval)
                else:
                    intervals.insert(idx, newInterval)
                break

            if intervals[idx][0] > newInterval[0]:
                intervals.insert(idx, newInterval)
                break

            idx += 1
        # print(intervals)

        res.append(intervals[0])
        # print(res)

        # Loop
        for start, end in intervals[1:]:
            # print("loop -", start, end)
            lastEnd = res[-1][1]
            if lastEnd >= start:
                res[-1][1] = max(lastEnd, end)
                # print("loop", res)
            else:
                res.append([start, end])

        return res


intervals = [[1, 3], [6, 9]]
newInterval = [2, 5]

# intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
# newInterval = [4, 8]
print(Solution().insert(intervals, newInterval))
