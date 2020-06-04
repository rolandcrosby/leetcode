# Two City Scheduling
# There are 2N people a company is planning to interview. The cost of flying the i-th
# person to city A is costs[i][0], and the cost of flying the i-th person to city B is
# costs[i][1].
#
# Return the minimum cost to fly every person to a city such that exactly N people
# arrive in each city.
#
# Example 1:
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation:
# - The first person goes to city A for a cost of 10.
# - The second person goes to city A for a cost of 30.
# - The third person goes to city B for a cost of 50.
# - The fourth person goes to city B for a cost of 20.
# - The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
#   interviewing in each city.
#
# Note:
# - 1 <= costs.length <= 100
# - It is guaranteed that costs.length is even.
# - 1 <= costs[i][0], costs[i][1] <= 1000

import testlib
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_diffs = sorted([(c[0] - c[1], i) for (i, c) in enumerate(costs)])
        total_cost = 0
        for (_, i) in cost_diffs[0 : len(cost_diffs) // 2]:
            total_cost += costs[i][0]
        for (_, i) in cost_diffs[len(cost_diffs) // 2 :]:
            total_cost += costs[i][1]
        return total_cost


if __name__ == "__main__":
    testdata = [([[10, 20], [30, 200], [400, 50], [30, 20]], 110)]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().twoCitySchedCost(tc[0]), tc[1], tc),
        testdata,
    )
