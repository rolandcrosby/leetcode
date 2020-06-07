# Queue Reconstruction by Height
# Suppose you have a random list of people standing in a queue. Each person is described
# by a pair of integers (h, k), where h is the height of the person and k is the number
# of people in front of this person who have a height greater than or equal to h. Write
# an algorithm to reconstruct the queue.
#
# Note:
# The number of people is less than 1,100.
#
# Example
# Input:
# [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
#
# Output:
# [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

import testlib
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        out = []
        for item in sorted(people, key=lambda n: (-n[0], n[1])):
            out.insert(item[1], item)
        return out


if __name__ == "__main__":
    testdata = [
        (
            [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
            [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
        )
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().reconstructQueue(tc[0]), tc[1], tc),
        testdata,
    )
