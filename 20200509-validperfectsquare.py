# Valid Perfect Square
#
# Given a positive integer num, write a function which returns True if num is a perfect
# square else False.
#
# Note: Do not use any built-in library function such as sqrt.
#
# Example 1:
# Input: 16
# Output: true
#
# Example 2:
# Input: 14
# Output: false

import testlib


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        n = 1
        while n * n < num:
            n += 1
        return n * n == num


if __name__ == "__main__":
    testdata = [(16, True), (14, False)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().isPerfectSquare(tc[0]), tc[1], tc),
        testdata,
    )
