# H-Index II
# Given an array of citations sorted in ascending order (each citation is a non-negative
# integer) of a researcher, write a function to compute the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: "A scientist has index h if h of
# his/her N papers have at least h citations each, and the other N − h papers have no
# more than h citations each."
#
# Example:
# Input: citations = [0,1,3,5,6]
# Output: 3
# Explanation: [0,1,3,5,6] means the researcher has 5 papers in total and each of them
# had received 0, 1, 3, 5, 6 citations respectively. Since the researcher has 3 papers
# with at least 3 citations each and the remaining two with no more than 3 citations
# each, her h-index is 3.
# Note:
#
# If there are several possible values for h, the maximum one is taken as the h-index.
#
# Follow up:
#
# This is a follow up problem to H-Index, where citations is now guaranteed to be sorted
# in ascending order.
# Could you solve it in logarithmic time complexity?

import testlib
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """
        The h-index is the maximum value of h such that the given author/journal has
        published h papers that have each been cited at least h times.
        """
        for i in range(len(citations) - 1, -1, -1):
            idx = len(citations) - i - 1
            print(i, idx, citations[idx])
            if idx >= 0 and citations[idx] >= i and citations[idx]:
                return min(citations[idx], i + 1)
        return 0


if __name__ == "__main__":
    testdata = [
        ([0, 0, 4, 4], 2),
        ([0, 1, 3, 5, 6], 3),
        ([], 0),
        ([100], 1),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().hIndex(tc[0]), tc[1], tc), testdata
    )

