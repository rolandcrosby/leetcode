# Interval List Intersections
# Given two lists of closed intervals, each list of intervals is pairwise disjoint and
# in sorted order.
#
# Return the intersection of these two interval lists.
#
# (Formally, a closed interval [a, b] (with a <= b) denotes the set of real numbers x
# with a <= x <= b.  The intersection of two closed intervals is a set of real numbers
# that is either empty, or can be represented as a closed interval.  For example, the
# intersection of [1, 3] and [2, 4] is [2, 3].)
#
# Example 1:
# Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
#
# Reminder: The inputs and the desired output are lists of Interval objects, and not
# arrays or lists.
#
# Note:
# - 0 <= A.length < 1000
# - 0 <= B.length < 1000
# - 0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9

import testlib
from typing import List


class Solution:
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        out = []
        i_a = 0
        i_b = 0
        while i_a < len(A) and i_b < len(B):
            a = A[i_a]
            b = B[i_b]
            if a[1] < b[0]:
                i_a += 1
                continue
            if b[1] < a[0]:
                i_b += 1
                continue
            start = max(a[0], b[0])
            end = min(a[1], b[1])
            if out and start == out[-1][1]:
                out[-1][1] = end
            else:
                out.append([start, end])
            if a[1] < b[1]:
                i_a += 1
            else:
                i_b += 1
        return out


if __name__ == "__main__":
    testdata = [
        (
            [[0, 2], [5, 10], [13, 23], [24, 25]],
            [[1, 5], [8, 12], [15, 24], [25, 26]],
            [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
        )
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().intervalIntersection(tc[0], tc[1]), tc[2], tc
        ),
        testdata,
    )
