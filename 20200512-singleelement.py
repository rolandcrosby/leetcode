# Single Element in a Sorted Array
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.
#
# Example 1:
# Input: [1,1,2,3,3,4,4,8,8]
# Output: 2
#
# Example 2:
# Input: [3,3,7,7,10,11,11]
# Output: 10
#
# Note: Your solution should run in O(log n) time and O(1) space.

import testlib
from functools import reduce
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        start = 0
        end = len(nums) - 1
        while start + 1 < end:
            probe = (start + end) // 2
            if probe % 2 == 1:
                probe -= 1
            if nums[probe] == nums[probe + 1]:
                start = probe + 2
            else:
                end = probe + 1
        return nums[start]

    def singleNonDuplicateGeneral(self, nums: List[int]) -> int:
        # not O(log n) but quite fast anyway
        return reduce(lambda x, y: x ^ y, nums, 0)


if __name__ == "__main__":
    testdata = [
        ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
        ([3, 3, 7, 7, 10, 11, 11], 10),
        ([1, 1, 2, 3, 3], 2),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().singleNonDuplicate(tc[0]), tc[1], tc),
        testdata,
    )
