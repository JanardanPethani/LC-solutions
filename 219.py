"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""


def containsNearbyDuplicate(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, i + 1 + k):
            if j < len(nums) and nums[i] == nums[j]:
                return True

    return False


nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))
