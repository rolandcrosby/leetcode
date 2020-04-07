# Group Anagrams
# Given an array of strings, group anagrams together.
#
# Example:
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:
#
# All inputs will be in lowercase.
# The order of your output does not matter.

from typing import List, FrozenSet


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}
        for s in strs:
            key = "".join(sorted(s))
            out.setdefault(key, []).append(s)
        return out.values()


if __name__ == "__main__":
    testdata = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [
                ["ate", "eat", "tea"],
                ["nat", "tan"],
                ["bat"]
            ]
        )
    ]
    def to_set(ans: List[List[str]]) -> FrozenSet[FrozenSet[str]]:
        return frozenset([frozenset(s) for s in ans])
    passed = 0
    for tc in testdata:
        assert to_set(Solution().groupAnagrams(tc[0])) == to_set(tc[1])
        passed += 1
    print("%d of %d tests passed" % (passed, len(testdata)))
