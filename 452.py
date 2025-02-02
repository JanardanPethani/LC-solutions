"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.

 
Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].


Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
"""
from typing import List


class Solution:
    def canIncludeInLst(self, burst_at_once_lst: List[List[int]], point: List[int]) -> bool:
        can_include = True
        for start, end in burst_at_once_lst:
            if point[0] > end:
                can_include = False
            else:
                continue
        return can_include
    
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_arr = sorted(points, key=lambda x: x[0])
        # print("sorted_arr: ", sorted_arr)
        idx = 1
        count = 0
        burst_at_once = [sorted_arr[0]]
        while idx < len(sorted_arr):
            # print("burst_at_once: ", burst_at_once, sorted_arr[idx])
            if self.canIncludeInLst(burst_at_once, sorted_arr[idx]):
                burst_at_once.append(sorted_arr[idx])
            else:
                burst_at_once = [sorted_arr[idx]]
                count += 1
            idx += 1
        
        count += 1

        return count


points = [[1,4],[2,4],[4, 6],[4,5]]
print(Solution().findMinArrowShots(points))
