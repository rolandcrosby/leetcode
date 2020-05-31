# Edit Distance
# Given two words word1 and word2, find the minimum number of operations required to
# convert word1 to word2.
#
# You have the following 3 operations permitted on a word:
# - Insert a character
# - Delete a character
# - Replace a character
#
# Example 1:
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# - horse -> rorse (replace 'h' with 'r')
# - rorse -> rose (remove 'r')
# - rose -> ros (remove 'e')
#
# Example 2:
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# - intention -> inention (remove 't')
# - inention -> enention (replace 'i' with 'e')
# - enention -> exention (replace 'n' with 'x')
# - exention -> exection (replace 'n' with 'c')
# - exection -> execution (insert 'u')

import testlib


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        distances = [
            [None for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)
        ]
        for i in range(len(word1) + 1):
            distances[i][0] = i
        for i in range(len(word2) + 1):
            distances[0][i] = i

        for r in range(1, len(word1) + 1):
            char1 = word1[r - 1]
            for c in range(1, len(word2) + 1):
                char2 = word2[c - 1]
                if char2 == char1:
                    distances[r][c] = distances[r - 1][c - 1]
                else:
                    distances[r][c] = 1 + min(
                        distances[r - 1][c - 1],
                        distances[r][c - 1],
                        distances[r - 1][c],
                    )

        # for col in "  " + word2:
        #     print(col, end="  ")
        # print()
        # for (r, row) in enumerate(distances):
        #     if r == 0:
        #         print(" ", end=" ")
        #     else:
        #         print(word1[r - 1], end=" ")
        #     for val in row:
        #         print("{:2d}".format(val), end=" ")
        #     print()
        # print()
        return distances[-1][-1]


if __name__ == "__main__":
    testdata = [
        ("horse", "ros", 3),
        ("intention", "execution", 5),
        ("", "", 0),
        ("zoologicoarchaeologist", "zoogeologist", 10),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().minDistance(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
