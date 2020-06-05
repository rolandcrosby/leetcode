# Random Pick with Weight
# Given an array w of positive integers, where w[i] describes the weight of index i,
# write a function pickIndex which randomly picks an index in proportion to its weight.
#
# Note:
# - 1 <= w.length <= 10000
# - 1 <= w[i] <= 10^5
# - pickIndex will be called at most 10000 times.
#
# Example 1:
# Input:
# ["Solution","pickIndex"]
# [[[1]],[]]
# Output: [null,0]
#
# Example 2:
# Input:
# ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
# [[[1,3]],[],[],[],[],[]]
# Output: [null,0,1,1,1,0]
#
# Explanation of Input Syntax:
# The input is two lists: the subroutines called and their arguments. Solution's
# constructor has one argument, the array w. pickIndex has no arguments. Arguments are
# always wrapped with a list, even if there aren't any.

import testlib
import bisect
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.total = 0
        self.weight_map = []
        for current in w:
            self.total += current
            self.weight_map.append(self.total)

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.weight_map, random.random() * self.total)


def run_test(t: testlib.unittest.TestCase, tc: List[int]):
    iterations = 10000
    solution = Solution(tc)
    results = [0 for _ in tc]
    for _ in range(iterations):
        results[solution.pickIndex()] += 1
    total = sum(tc)
    expected = [n / total for n in tc]
    actual = [n / iterations for n in results]
    for i in range(len(actual)):
        # there is probably a better way to do this - chi square test or something?
        t.assertAlmostEqual(expected[i], actual[i], 1)


if __name__ == "__main__":
    testdata = [[1], [1, 3]]
    testlib.run(run_test, testdata)
