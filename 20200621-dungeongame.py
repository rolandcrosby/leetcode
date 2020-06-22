# Dungeon Game
# The demons had captured the princess (P) and imprisoned her in the bottom-right corner
# of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant
# knight (K) was initially positioned in the top-left room and must fight his way
# through the dungeon to rescue the princess.
#
# The knight has an initial health point represented by a positive integer. If at any
# point his health point drops to 0 or below, he dies immediately.
#
# Some of the rooms are guarded by demons, so the knight loses health (negative
# integers) upon entering these rooms; other rooms are either empty (0's) or contain
# magic orbs that increase the knight's health (positive integers).
#
# In order to reach the princess as quickly as possible, the knight decides to move only
# rightward or downward in each step.
#
# Write a function to determine the knight's minimum initial health so that he is able
# to rescue the princess.
#
# For example, given the dungeon below, the initial health of the knight must be at
# least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
#
# -2 (K)	-3	3
# -5	-10	1
# 10	30	-5 (P)
#
# Note:
# - The knight's health has no upper bound.
# - Any room can contain threats or power-ups, even the first room the knight enters and
#   the bottom-right room where the princess is imprisoned.

import testlib
from typing import List
from math import inf


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        min_health = 1
        min_to_end = [
            [None for _ in range(len(dungeon[0]) + 1)] for _ in range(len(dungeon) + 1)
        ]
        for r in range(len(min_to_end)):
            min_to_end[r][-1] = inf
        for c in range(len(dungeon[0])):
            min_to_end[-1][c] = inf
        min_to_end[len(dungeon) - 1][-1] = min_health
        min_to_end[-1][len(dungeon[0]) - 1] = min_health
        for r in range(len(dungeon) - 1, -1, -1):
            for c in range(len(dungeon[0]) - 1, -1, -1):
                min_to_end[r][c] = max(
                    min(min_to_end[r + 1][c], min_to_end[r][c + 1]) - dungeon[r][c],
                    min_health,
                )
        return min_to_end[0][0]


if __name__ == "__main__":
    testdata = [
        ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
        ([[0]], 1),
        ([[100]], 1),
        ([[-200]], 201),
        ([[0, 0]], 1),
        ([[0, -2, 10, -5]], 3),
        ([[1, -3, 3], [0, -2, 0], [-3, -3, -3]], 3),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().calculateMinimumHP(tc[0]), tc[1], tc),
        testdata,
    )
