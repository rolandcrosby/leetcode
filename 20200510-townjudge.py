# Find the Town Judge
# In a town, there are N people labelled from 1 to N.  There is a rumor that one of these people is secretly the town judge.
#
# If the town judge exists, then:
# - The town judge trusts nobody.
# - Everybody (except for the town judge) trusts the town judge.
# - There is exactly one person that satisfies properties 1 and 2.
#
# You are given trust, an array of pairs trust[i] = [a, b] representing that the person labelled a trusts the person labelled b.
#
# If the town judge exists and can be identified, return the label of the town judge.  Otherwise, return -1.
#
# Example 1:
# Input: N = 2, trust = [[1,2]]
# Output: 2
#
# Example 2:
# Input: N = 3, trust = [[1,3],[2,3]]
# Output: 3
#
# Example 3:
# Input: N = 3, trust = [[1,3],[2,3],[3,1]]
# Output: -1
#
# Example 4:
# Input: N = 3, trust = [[1,2],[2,3]]
# Output: -1
#
# Example 5:
# Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
# Output: 3
#
# Note:
# - 1 <= N <= 1000
# - trust.length <= 10000
# - trust[i] are all different
# - trust[i][0] != trust[i][1]
# - 1 <= trust[i][0], trust[i][1] <= N

import testlib
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        possible_judges = set(range(1, N+1))
        trusted_by = {}
        for t in trust:
            if t[0] in possible_judges:
                possible_judges.remove(t[0])
            if len(possible_judges) == 0:
                return -1
            trusted_by.setdefault(t[1], set())
            trusted_by[t[1]].add(t[0])
        if len(possible_judges) > 1:
            return -1
        judge = possible_judges.pop()
        if len(trusted_by.setdefault(judge, set())) != N - 1:
            return -1
        return judge


if __name__ == "__main__":
    testdata = [
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
        (3, [[1, 2], [2, 3]], -1),
        (4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]], 3),
        (1, [], 1)
    ]
    testlib.run(lambda t, tc: t.assertEqual(Solution().findJudge(tc[0], tc[1]), tc[2], tc), testdata)
