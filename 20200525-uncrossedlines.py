# Uncrossed Lines
# We write the integers of A and B (in the order they are given) on two separate
# horizontal lines.
#
# Now, we may draw connecting lines: a straight line connecting two numbers A[i] and
# B[j] such that:
# A[i] == B[j];
# The line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting lines cannot intersect even at the endpoints: each number can
# only belong to one connecting line.
#
# Return the maximum number of connecting lines we can draw in this way.
#
# Example 1:
# 1 4 2
# |  \
# 1 2 4
# Input: A = [1,4,2], B = [1,2,4]
# Output: 2
# Explanation: We can draw 2 uncrossed lines as in the diagram.
# We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4 will
# intersect the line from A[2]=2 to B[1]=2.
#
# Example 2:
#  2 5 1 2 5
#    |  \  |
# 10 5 2 1 5 2
# Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
# Output: 3
#
# Example 3:
# 1 3 7 1 7 5
# |      \
# 1 9 2 5 1
# Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
# Output: 2
#
# Note:
# - 1 <= A.length <= 500
# - 1 <= B.length <= 500
# - 1 <= A[i], B[i] <= 2000

from typing import List
import testlib


class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        solutions = [[0 for _ in B] for _ in A]

        def get(r: int, c: int) -> int:
            if r < 0 or c < 0:
                return 0
            return solutions[r][c]

        for (r, a) in enumerate(A):
            for (c, b) in enumerate(B):
                solutions[r][c] = max(
                    get(r - 1, c), get(r, c - 1), get(r - 1, c - 1) + int(a == b)
                )

        return solutions[-1][-1]


if __name__ == "__main__":
    testdata = [
        ([1, 4, 2], [1, 2, 4], 2),
        ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
        ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().maxUncrossedLines(tc[0], tc[1]), tc[2], tc
        ),
        testdata,
    )
