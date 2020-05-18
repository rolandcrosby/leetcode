# Permutation in String
# Given two strings s1 and s2, write a function to return true if s2 contains the
# permutation of s1. In other words, one of the first string's permutations is the
# substring of the second string.
#
# Example 1:
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
#
# Example 2:
# Input: s1 = "ab" s2 = "eidboaoo"
# Output: False
#
# Note:
# - The input strings only contain lower case letters.
# - The length of both given strings is in range [1, 10,000].

import testlib
from typing import Dict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needed_letters: Dict[str, int] = {}
        for c in s1:
            needed_letters[c] = needed_letters.get(c, 0) + 1

        test_letters: Dict[str, int] = {}
        for c in s2[0 : len(s1)]:
            test_letters[c] = test_letters.get(c, 0) + 1

        for i in range(1 + len(s2) - len(s1)):
            if needed_letters == test_letters:
                return True
            if i + len(s1) < len(s2) and s2[i] != s2[i + len(s1)]:
                test_letters[s2[i + len(s1)]] = test_letters.get(s2[i + len(s1)], 0) + 1
                test_letters[s2[i]] -= 1
                if test_letters[s2[i]] == 0:
                    del test_letters[s2[i]]
        return False


if __name__ == "__main__":
    testdata = [("ab", "eidbaooo", True), ("ab", "eidboaoo", False)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().checkInclusion(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
