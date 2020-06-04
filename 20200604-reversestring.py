# Reverse String
# Write a function that reverses a string. The input string is given as an array of
# characters char[].
#
# Do not allocate extra space for another array, you must do this by modifying the input
# array in-place with O(1) extra memory.
#
# You may assume all the characters consist of printable ascii characters.
#
# Example 1:
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Example 2:
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

from typing import List, Tuple
import testlib


class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


def runTestCase(t: testlib.unittest.TestCase, tc: Tuple[List[str], List[str]]):
    s = tc[0]
    Solution().reverseString(s)
    t.assertEqual(s, tc[1])


if __name__ == "__main__":
    testdata = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
    ]
    testlib.run(runTestCase, testdata)
