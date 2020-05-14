# First Bad Version
# You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check. Since each
# version is developed based on the previous version, all the versions after a bad
# version are also bad.
#
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one,
# which causes all the following ones to be bad.
#
# You are given an API bool isBadVersion(version) which will return whether version is
# bad. Implement a function to find the first bad version. You should minimize the
# number of calls to the API.
#
# Example:
#
# Given n = 5, and version = 4 is the first bad version.
#
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
#
# Then 4 is the first bad version.

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

import testlib
from typing import Callable


class Solution:
    def __init__(self, fn: Callable[[int], bool] = None):
        if fn is not None:
            self.fn = fn
        else:
            self.fn = isBadVersion

    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end:
            guess = (start + end) // 2
            if self.fn(guess):
                end = guess
            else:
                start = guess + 1
        return start


def isBadVersion(n: int) -> bool:
    return n >= 4


if __name__ == "__main__":
    testdata = [(lambda x: x >= 4, 5, 4)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution(tc[0]).firstBadVersion(tc[1]), tc[2], tc),
        testdata,
    )
