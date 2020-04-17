# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
# Output: 1
#
# Example 2:
# Input:
# 11000
# 11000
# 00100
# 00011
# Output: 3

from typing import List, Tuple
import testlib


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        if rows == 0:
            return 0
        cols = len(grid[0])
        if cols == 0:
            return 0

        def at(r: int, c: int) -> str:
            if r < 0 or r >= rows:
                return "0"
            if c < 0 or c >= cols:
                return "0"
            return grid[r][c]

        def fill(
            pts: List[Tuple[int, int]], old: str, new: str
        ) -> List[Tuple[int, int]]:
            if len(pts) == 0:
                return
            r, c = pts.pop(0)
            if at(r, c) == old:
                grid[r][c] = new
                if at(r - 1, c) == old:
                    pts.append((r - 1, c))
                if at(r + 1, c) == old:
                    pts.append((r + 1, c))
                if at(r, c - 1) == old:
                    pts.append((r, c - 1))
                if at(r, c + 1) == old:
                    pts.append((r, c + 1))
            return pts

        to_check = [
            (r, c)
            for (r, row) in enumerate(grid)
            for (c, cell) in enumerate(row)
            if grid[r][c] == "1"
        ]
        islands = 0
        for pt in to_check:
            if at(pt[0], pt[1]) != "1":
                continue
            todo = [pt]
            while len(todo) > 0:
                todo = fill(todo, "1", str(islands + 2))
            islands += 1

        return islands


if __name__ == "__main__":
    testdata = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().numIslands(tc[0]), tc[1]), testdata
    )
