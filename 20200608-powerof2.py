# Power of 2
# Given an integer, write a function to determine if it is a power of two.
#
# Example 1:
# Input: 1
# Output: true
# Explanation: 2^0 = 1
#
# Example 2:
# Input: 16
# Output: true
# Explanation: 2^4 = 16
#
# Example 3:
# Input: 218
# Output: false

import testlib


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        while n:
            if n > 1 and n & 1:
                return False
            n >>= 1
        return True


if __name__ == "__main__":
    testdata = [(1, True), (16, True), (218, False), (0, False), (-16, False)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().isPowerOfTwo(tc[0]), tc[1], tc), testdata
    )
