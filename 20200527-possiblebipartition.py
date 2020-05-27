# Possible Bipartition
# Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into
# two groups of any size.
#
# Each person may dislike some other people, and they should not go into the same group.
#
# Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people
# numbered a and b into the same group.
#
# Return true if and only if it is possible to split everyone into two groups in this
# way.
#
# Example 1:
# Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
# Output: true
# Explanation: group1 [1,4], group2 [2,3]
#
# Example 2:
# Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
# Output: false
#
# Example 3:
# Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# Output: false
#
# Note:
# - 1 <= N <= 2000
# - 0 <= dislikes.length <= 10000
# - 1 <= dislikes[i][j] <= N
# - dislikes[i][0] < dislikes[i][1]
# - There does not exist i != j for which dislikes[i] == dislikes[j].

from typing import List
import testlib


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if len(dislikes) == 0:
            return True
        colors = [None for _ in range(N + 1)]
        graph = [set() for _ in range(N + 1)]
        for pair in dislikes:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])
        todo = []
        for start in range(1, N):
            if colors[start] is None:
                colors[start] = 1
                todo.append(start)
                while todo:
                    n = todo.pop(0)
                    for adj in graph[n]:
                        if colors[adj] is None:
                            colors[adj] = 1 - colors[n]
                            todo.append(adj)
                        elif colors[adj] == colors[n]:
                            return False
        return True


if __name__ == "__main__":
    testdata = [
        (4, [[1, 2], [1, 3], [2, 4]], True),
        (3, [[1, 2], [1, 3], [2, 3]], False),
        (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False),
        (5, [[1, 2], [3, 4], [4, 5], [3, 5]], False),
        (
            10,
            [[5, 9], [5, 10], [5, 6], [5, 7], [1, 5], [4, 5], [2, 5], [5, 8], [3, 5]],
            True,
        ),
        (
            50,
            [
                [39, 46],
                [4, 41],
                [3, 35],
                [8, 44],
                [22, 44],
                [7, 49],
                [28, 41],
                [7, 25],
                [6, 35],
                [2, 22],
                [34, 35],
                [3, 7],
                [1, 11],
                [11, 48],
                [8, 24],
                [6, 7],
                [38, 40],
                [37, 48],
                [3, 45],
                [44, 45],
                [4, 46],
                [23, 35],
                [28, 46],
                [7, 28],
                [35, 36],
                [18, 20],
                [8, 15],
                [17, 41],
                [13, 35],
                [6, 22],
                [22, 48],
                [22, 39],
                [4, 35],
                [8, 38],
                [23, 41],
                [10, 41],
                [6, 41],
                [18, 48],
                [16, 41],
                [37, 44],
                [8, 12],
                [18, 36],
                [16, 18],
                [7, 44],
                [3, 18],
                [10, 46],
                [20, 37],
                [2, 37],
                [11, 49],
                [30, 45],
                [28, 37],
                [23, 37],
                [22, 23],
                [5, 37],
                [29, 40],
                [16, 35],
                [22, 26],
                [46, 49],
                [18, 26],
                [8, 9],
                [24, 46],
                [8, 28],
                [11, 29],
                [22, 24],
                [7, 15],
                [4, 37],
                [9, 40],
                [8, 32],
                [23, 40],
                [40, 42],
                [33, 40],
                [17, 45],
                [40, 48],
                [12, 41],
                [43, 45],
                [38, 41],
                [45, 47],
                [12, 18],
                [7, 31],
                [34, 37],
                [8, 48],
                [4, 11],
                [46, 48],
                [2, 7],
                [17, 40],
                [12, 46],
                [22, 49],
                [46, 50],
                [37, 50],
                [22, 36],
                [22, 43],
                [41, 44],
                [13, 22],
                [11, 16],
                [7, 47],
                [14, 37],
                [37, 43],
                [13, 37],
                [26, 40],
                [19, 41],
                [46, 47],
                [16, 22],
                [19, 22],
                [22, 33],
                [11, 19],
                [35, 44],
                [7, 33],
                [41, 49],
                [38, 45],
                [25, 35],
                [3, 37],
                [15, 22],
                [6, 18],
                [11, 30],
                [5, 41],
                [8, 33],
                [1, 46],
                [31, 46],
                [41, 42],
                [18, 28],
                [15, 41],
                [35, 49],
                [25, 41],
                [20, 45],
                [26, 46],
                [8, 43],
                [5, 45],
                [28, 40],
                [1, 18],
                [23, 46],
                [13, 18],
                [35, 38],
                [8, 49],
                [11, 44],
                [18, 33],
                [4, 7],
                [5, 7],
                [10, 11],
                [37, 49],
                [9, 22],
                [4, 45],
                [32, 45],
                [32, 37],
                [29, 35],
                [26, 35],
                [7, 29],
                [1, 37],
                [8, 14],
                [5, 11],
                [18, 29],
                [18, 49],
                [21, 41],
                [17, 35],
                [7, 10],
                [22, 38],
                [40, 43],
                [5, 35],
                [33, 35],
                [6, 40],
                [34, 40],
                [22, 34],
                [16, 40],
                [19, 46],
                [18, 39],
                [24, 35],
                [19, 35],
                [18, 50],
                [8, 17],
                [11, 12],
                [27, 35],
                [8, 47],
                [7, 9],
                [7, 36],
                [8, 34],
                [7, 26],
                [31, 41],
                [29, 41],
                [10, 45],
                [9, 35],
                [33, 46],
                [11, 32],
                [34, 45],
                [42, 46],
                [15, 40],
                [40, 50],
                [30, 40],
                [25, 40],
                [15, 37],
            ],
            True,
        ),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(
            Solution().possibleBipartition(tc[0], tc[1]), tc[2], tc
        ),
        testdata,
    )
