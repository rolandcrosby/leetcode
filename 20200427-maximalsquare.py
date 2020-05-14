# Maximal Square
# Given a 2D binary matrix filled with 0's and 1's, find the largest square containing
# only 1's and return its area.
#
# Example:
# Input:
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Output: 4

import testlib
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        def get(matrix: List[List[int]], r: int, c: int) -> int:
            try:
                return matrix[r][c]
            except IndexError:
                return 0

        def zeroes(w: int, h: int) -> List[List[int]]:
            return [[0 for _ in range(w)] for _ in range(h)]

        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        horiz_run = zeroes(len(matrix[0]), len(matrix))
        vert_run = zeroes(len(matrix[0]), len(matrix))
        bests = zeroes(len(matrix[0]), len(matrix))
        ans = 0
        for (r, row) in enumerate(matrix):
            for (c, val) in enumerate(row):
                horiz_run[r][c] = 0 if val == "0" else 1 + get(horiz_run, r, c - 1)
                vert_run[r][c] = 0 if val == "0" else 1 + get(vert_run, r - 1, c)
                corner_size = min(
                    min(horiz_run[r][c], vert_run[r][c]), get(bests, r - 1, c - 1) + 1
                )
                bests[r][c] = corner_size
                ans = max(ans, corner_size)
        return ans * ans


if __name__ == "__main__":
    testdata = [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
        ),
        (
            [
                ["0", "0", "0", "1"],
                ["1", "1", "0", "1"],
                ["1", "1", "1", "1"],
                ["0", "1", "1", "1"],
                ["0", "1", "1", "1"],
            ],
            9,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().maximalSquare(tc[0]), tc[1], tc),
        testdata,
    )
