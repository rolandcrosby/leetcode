# Check If It Is a Straight Line
#
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
#
# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
#
# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
#
# Constraints:
# - 2 <= coordinates.length <= 1000
# - coordinates[i].length == 2
# - -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# - coordinates contains no duplicate point.

import testlib
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) < 3:
            return True
        first = coordinates[0]
        if coordinates[1][0] - first[0] == 0:
            return len([1 for c in coordinates if c[0] != first[0]]) == 0
        slope = (coordinates[1][1] - first[1]) / (coordinates[1][0] - first[0])
        for coord in coordinates[2:]:
            run = coord[0] - first[0]
            if run == 0:
                return False
            if (coord[1] - first[1]) / run != slope:
                return False
        return True


if __name__ == "__main__":
    testdata = [
        ([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]], True),
        ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]], False),
        ([[1, 1], [1, 2], [1, 3]], True),
        ([[1, 1], [1, 2], [2, 2]], False),
        ([[1, 1], [2, 2], [1, 2]], False)
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().checkStraightLine(tc[0]), tc[1], tc),
        testdata,
    )
