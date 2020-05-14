# Leftmost Column with At Least a One
# (This problem is an interactive problem.)
#
# A binary matrix means that all elements are 0 or 1. For each individual row of the
# matrix, this row is sorted in non-decreasing order.
#
# Given a row-sorted binary matrix binaryMatrix, return leftmost column index
# (0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.
#
# You can't access the Binary Matrix directly.  You may only access the matrix using a
# BinaryMatrix interface:
# - BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed)
# - BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the
#   matrix is n * m.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong
# Answer.
# Also, any solutions that attempt to circumvent the judge will result in
# disqualification.
#
# For custom testing purposes you're given the binary matrix mat as input in the
# following four examples. You will not have access the binary matrix directly.
#
# Example 1:
#   0 1
#   1 1
# Input: mat = [[0,0],[1,1]]
# Output: 0
#
# Example 2:
#   0 0
#   0 1
# Input: mat = [[0,0],[0,1]]
# Output: 1
#
# Example 3:
#   0 0
#   0 0
# Input: mat = [[0,0],[0,0]]
# Output: -1
#
# Example 4:
#   0 0 0 1
#   0 0 1 1
#   0 1 1 1
#
# Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
# Output: 1
#
# Constraints:
# - 1 <= mat.length, mat[i].length <= 100
# - mat[i][j] is either 0 or 1.
# - mat[i] is sorted in a non-decreasing way.

import testlib
from typing import List


class BinaryMatrix:
    def __init__(self, mat: List[List[int]] = [[]]):
        self._mat = mat

    def get(self, x: int, y: int) -> int:
        if y >= len(self._mat) or y < 0:
            raise IndexError("y out of range")
        if x >= len(self._mat[0]) or x < 0:
            raise IndexError("x out of range")
        return self._mat[y][x]

    def dimensions(self) -> List[int]:
        h = len(self._mat)
        w = 0
        if h > 0:
            w = len(self._mat[0])
        return [w, h]


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        (w, h) = binaryMatrix.dimensions()
        cache = [[None for _ in range(w)] for _ in range(h)]

        def get(x: int, y: int) -> int:
            if cache[y][x] is None:
                cache[y][x] = binaryMatrix.get(x, y)
            return cache[y][x]
        min_col = w
        for y in range(h):
            start, end = 0, w - 1
            while start < end:
                guess = (start + end) // 2
                if get(guess, y) == 0:
                    start = guess + 1
                else:
                    end = guess
            if start < min_col and get(start, y) == 1:
                min_col = start
        if min_col == w:
            return -1
        else:
            return min_col


if __name__ == "__main__":
    testdata = [
        ([[0, 0], [1, 1]], 0),
        ([[0, 0], [0, 1]], 1),
        ([[0, 0], [0, 0]], -1),
        ([[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]], 1),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().leftMostColumnWithOne(BinaryMatrix(tc[0])), tc[1], tc
        ),
        testdata,
    )
