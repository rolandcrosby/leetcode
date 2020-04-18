# Minimum Path Sum
# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example:
#
# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.

import testlib
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if r == 0:
                    if c > 0:
                        grid[r][c] += grid[r][c - 1]
                elif c == 0:
                    grid[r][c] += grid[r - 1][c]
                else:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]


if __name__ == "__main__":
    testdata = [([[1, 3, 1], [1, 5, 1], [4, 2, 1]], 7)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().minPathSum(tc[0]), tc[1], tc), testdata
    )
