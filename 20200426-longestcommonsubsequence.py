# Longest Common Subsequence
#
# Given two strings text1 and text2, return the length of their longest common subsequence.
#
# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.
#
# If there is no common subsequence, return 0.
#
# Example 1:
# Input: text1 = "abcde", text2 = "ace"
# Output: 3
# Explanation: The longest common subsequence is "ace" and its length is 3.
#
# Example 2:
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
#
# Example 3:
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
#
# Constraints:
# - 1 <= text1.length <= 1000
# - 1 <= text2.length <= 1000
# - The input strings consist of lowercase English characters only.

import testlib
from typing import Callable


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        subs = [[0 for _ in text2] for _ in text1]

        def get(i1: int, i2: int) -> int:
            if i1 >= 0 and i2 >= 0 and i1 < len(subs) and i2 < len(subs[0]):
                return subs[i1][i2]
            else:
                return 0

        for i1 in range(len(text1)):
            for i2 in range(len(text2)):
                if text1[i1] == text2[i2]:
                    num = get(i1 - 1, i2 - 1) + 1
                else:
                    num = max(get(i1, i2 - 1), get(i1 - 1, i2))
                subs[i1][i2] = num
        debug(text1, text2, get)
        return subs[-1][-1]


def debug(text1: str, text2: str, get: Callable[[int, int], int]):
    print("  ", end="")
    for c1 in text1:
        print("{} ".format(c1), end="")
    print()
    for (i2, c2) in enumerate(text2):
        print("{} ".format(c2), end="")
        for (i1, c1) in enumerate(text1):
            print("{} ".format(get(i1, i2)), end="")
        print()


if __name__ == "__main__":
    testdata = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
        ("bsbininm", "jmjkbkjkv", 1),
        ("bsbininm", "jmskv", 1),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().longestCommonSubsequence(tc[0], tc[1]), tc[2], tc
        ),
        testdata,
    )
