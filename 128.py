"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""

arr = [100, 4, 200, 1, 2, 3]

arrset = set(arr)
longest = 0

for n in arr:
    if (n - 1) not in arrset:
        leng = 0
        while (n + leng) in arrset:
            leng += 1
        longest = max(longest, leng)

print(longest)
