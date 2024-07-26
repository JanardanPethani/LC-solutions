"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in res.keys():
                res[sorted_word] = [word]
            else:
                res[sorted_word].append(word)
        return res.values()


d = Solution().groupAnagrams(
    ["nozzle", "punjabi", "waterlogged", "imprison", "crux", "xruc"]
)
print(d)
