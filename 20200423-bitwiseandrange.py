# Bitwise AND of Numbers Range
# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all
# numbers in this range, inclusive.
#
# Example 1:
#
# Input: [5,7]
# Output: 4
# Example 2:
#
# Input: [0,1]
# Output: 0

import testlib


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        out = 0
        bit = 1 << 31
        while (m & bit) == (n & bit) and bit > 0:
            out |= (m & bit)
            bit >>= 1
        return out


if __name__ == "__main__":
    testdata = [(5, 7, 4), (0, 1, 0), (5, 9, 0), (1, 3, 0), (5, 5, 5)]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().rangeBitwiseAnd(tc[0], tc[1]), tc[2], tc
        ),
        testdata,
    )
