"""
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

Input: nums1 = [1,2], nums2 = [3], k = 3
Output: [[1,3],[2,3]]
Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]
"""

import itertools


def kSmallestPairs(nums1, nums2, k):
    hset = {}
    for lst in itertools.product(nums1, nums2):
        if sum(lst) in hset:
            hset[sum(lst)].append(list(lst))
        else:
            hset[sum(lst)] = [list(lst)]
    myKeys = list(hset.keys())
    myKeys.sort()
    sorted_dict = {i: hset[i] for i in myKeys}
    hset = [inner_lst for lst in sorted_dict.values() for inner_lst in lst]
    return hset[:k]


print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
