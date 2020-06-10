# Search Insert Position
# Given a sorted array and a target value, return the index if the target is found. If
# not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
# Input: [1,3,5,6], 5
# Output: 2
#
# Example 2:
# Input: [1,3,5,6], 2
# Output: 1
#
# Example 3:
# Input: [1,3,5,6], 7
# Output: 4
#
# Example 4:
# Input: [1,3,5,6], 0
# Output: 0

import testlib
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min_idx = 0
        max_idx = len(nums)
        while min_idx < max_idx:
            test_idx = (min_idx + max_idx) // 2
            if nums[test_idx] < target:
                min_idx = test_idx + 1
            elif nums[test_idx] == target:
                return test_idx
            else:
                max_idx = test_idx
        return min_idx


if __name__ == "__main__":
    testdata = [
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
        ([1, 3, 5, 6], 0, 0),
        ([1, 3], 2, 1),
    ]
    testlib.run(
        lambda t, tc: t.assertEqual(Solution().searchInsert(tc[0], tc[1]), tc[2], tc),
        testdata,
    )
