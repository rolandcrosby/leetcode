# Largest Divisible Subset
# Given a set of distinct positive integers, find the largest subset such that every
# pair (Si, Sj) of elements in this subset satisfies:
#
# Si % Sj = 0 or Sj % Si = 0.
#
# If there are multiple solutions, return any subset is fine.
#
# Example 1:
# Input: [1,2,3]
# Output: [1,2] (of course, [1,3] will also be ok)
#
# Example 2:
# Input: [1,2,4,8]
# Output: [1,2,4,8]

import testlib
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        todo = sorted(nums)
        divisibles = [[n] for n in todo]
        max_len_and_idx = (1, 0)
        for i, n in enumerate(todo):
            for check_idx in range(0, i):
                if n % todo[check_idx] == 0:
                    if len(divisibles[check_idx]) + 1 > len(divisibles[i]):
                        divisibles[i] = divisibles[check_idx] + [n]
                        if len(divisibles[i]) > max_len_and_idx[0]:
                            max_len_and_idx = (len(divisibles[i]), i)
        return divisibles[max_len_and_idx[1]]


if __name__ == "__main__":
    testdata = [([1, 2, 3], [[1, 2], [1, 3]]), ([1, 2, 4, 8], [[1, 2, 4, 8]])]
    testlib.run(
        lambda t, tc: t.assertIn(Solution().largestDivisibleSubset(tc[0]), tc[1], tc),
        testdata,
    )
