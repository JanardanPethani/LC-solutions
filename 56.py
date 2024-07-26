"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

 
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
"""

intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]

sorted_array = intervals.copy()
sorted_array.sort(key=lambda x: x[0])
start, end = 0, 0
res = [sorted_array[0]]

for start, end in sorted_array[1:]:
    lastEnd = res[-1][1]

    if start <= lastEnd:
        res[-1][1] = max(lastEnd, end)
    else:
        res.append([start, end])

print(res)
