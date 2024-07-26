"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b


Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
"""
nums = [0, 2, 3, 4, 6, 8, 9]
start = 0
end = 0
res = []

while start < len(nums) and end < len(nums):
    if (end + 1) < len(nums) and nums[end + 1] == nums[end] + 1:
        end += 1
    else:
        if start == end:
            res.append(str(nums[start]))
            start += 1
            end += 1
        else:
            res.append(f"{nums[start]}->{nums[end]}")
            end += 1
            start = end

print(res)
